#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : article_service.py
# @Author: zaoshu
# @Date  : 2020-02-13
# @Desc  :
import json
from datetime import datetime

from sqlalchemy import distinct, func

from common.enc_util import md5
from common.exception import ServerException
from model.article import Article
from model.tag import Tag
from model.user_like import UserLike
from model.user_view import UserView
from service.qiniu_service import QiniuService


class ArticleService:

    @classmethod
    def get_max_catalogue_index(cls, user_name, catalogue_id):
        max_index = Article.select(func.max(Article.catalogue_index))\
            .filter(Article.user_name == user_name, Article.catalogue_id == catalogue_id).one()[0]
        return max_index + 1

    @classmethod
    def save(cls, user_name, id, title, content):
        summary = QiniuService.get_summary(content)
        if title is None:
            title = 'untitled'
        if id is None:
            file_name = md5(title + content + datetime.now().timestamp().__str__())
            url = QiniuService.upload_doc(content, file_name)
            catalogue_index = cls.get_max_catalogue_index(user_name, 1)
            article = Article(
                title=title,
                file_key=file_name,
                user_name=user_name,
                url=url,
                summary=summary,
                catalogue_id=1,
                catalogue_index=catalogue_index
            )
            article.insert()
            return Article.select().filter(Article.user_name == user_name, Article.file_key == file_name).one().id
        article = Article.select().get(id)
        if user_name != article.user_name:
            raise ServerException(msg=f'您没有权限修改{article.user_name}的文章')
        file_name = md5(title + content)
        if article.file_key == file_name:
            return id
        url = QiniuService.upload_doc(content, article.file_key, file_name)
        article.url = url
        article.file_key = file_name
        article.summary = summary
        Article.update(article)
        return id

    @classmethod
    def article_list(cls, user_name, is_published=True):
        if is_published:
            articles = Article.select().filter(Article.is_published).order_by(Article.updated_at.desc()).all()
        else:
            articles = Article.select().order_by(Article.updated_at.desc()).all()
        results = []
        for article in articles:
            data = article.get_json()
            data['author'] = article.user_name
            data['can_edit'] = user_name == article.user_name
            data.pop('user_name')
            results.append(data)
        return results

    @classmethod
    def view_article(cls, id, user_name):
        article = Article.select().get(id)
        if article is None or (not article.is_published and user_name != article.user_name):
            raise ServerException('文章不存在')
        user_view = UserView(
            user_name=user_name,
            article_id=id
        )
        UserView.insert(user_view)
        view_num = UserView.select(
            func.count(distinct(UserView.user_name)).label('count')
        ).filter(UserView.article_id == id).one()[0]
        article.view_num = view_num
        article.update()

    @classmethod
    def article_detail(cls, id, user_name):
        article = Article.select().get(id)
        if not article.is_published and user_name != article.user_name:
            raise ServerException('该文章未发布')
        cls.view_article(id, user_name)
        content = QiniuService.get_doc(article.url)
        result = article.get_json()
        result['content'] = content
        result['liked'] = cls.is_user_liked(user_name, id)
        return result

    @classmethod
    def publish_article(cls, user_name, id, title, tags, is_published):
        article = Article.select().get(id)
        article.title = title
        article.is_published = is_published
        tags = list(set(tags))
        tag_existed = Tag.select().filter(Tag.label.in_(tags)).all()
        for t in tag_existed:
            if t.user_name is None:
                t.user_name = user_name
                t.update()
        for t in list(set(tags).difference(set([tag.label for tag in tag_existed]))):
            Tag(
                user_name=user_name,
                label=t
            ).insert()
        article.tags = json.dumps(tags)
        article.update()
        return True

    @classmethod
    def like_article(cls, article_id, user_name):
        user_like: UserLike = UserLike.select().filter(
            UserLike.user_name == user_name, UserLike.article_id == article_id
        ).first()
        if user_like is None:
            liked = True
            user_like = UserLike(
                user_name=user_name,
                article_id=article_id,
                liked=liked
            )
            user_like.insert()
        else:
            liked = not user_like.liked
            user_like.liked = liked
            user_like.update()
        article = Article.select().get(article_id)
        article.like_num += 1 if liked else -1
        article.update()
        return liked

    @classmethod
    def is_user_liked(cls, user_name, article_id):
        if user_name is None:
            return False
        user_like: UserLike = UserLike.select().filter(
            UserLike.user_name == user_name, UserLike.article_id == article_id
        ).first()
        return False if user_like is None else user_like.liked

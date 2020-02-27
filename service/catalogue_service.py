#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : catalogue_service.py
# @Author: zaoshu
# @Date  : 2020-02-23
# @Desc  :
from sqlalchemy import func

from common.exception import ServerException
from common.log import Logger
from model.article import Article
from model.catalogue import Catalogue

log = Logger(__name__)


class CatalogueService:

    @classmethod
    def save(cls, user_name, args):
        id = args.get('id')
        name = args.get('name')
        index = args.get('index')
        assert name is not None
        if id is not None:
            catalogue = Catalogue.select().get(id)
            catalogue.name = name
            catalogue.index = index
            catalogue.update()
        else:
            catalogue = Catalogue(
                name=name,
                index=0
            )
            if index == 0:
                max_index = Catalogue.select(func.max(Catalogue.index)) \
                    .filter(Catalogue.user_name == user_name).one()[0]
                catalogue.index = max_index + 1
            catalogue.insert()

    @classmethod
    def delete(cls, catalogue_id):
        assert catalogue_id is not None
        articles = Article.select().filter(Article.catalogue_id == catalogue_id).first()
        if articles is not None:
            raise ServerException('非空目录，不允许删除')
        catalogue = Catalogue.select().get(catalogue_id)
        if catalogue is None:
            raise ServerException('目录不存在')
        catalogue.delete()
        return True

    @classmethod
    def get_catalogue(cls, user_name):
        catalogues = Catalogue.select().filter(Catalogue.user_name == user_name).order_by(Catalogue.index.asc()).all()
        catalogue_ids = [catalogue.id for catalogue in catalogues]
        articles = Article.select().filter(Article.catalogue_id.in_(catalogue_ids)) \
            .order_by(Article.catalogue_index.asc()).all()
        article_map = {}
        for article in articles:
            children = article_map.get(article.catalogue_id, None)
            if children is None:
                article_map[article.catalogue_id] = [article.get_json()]
            else:
                children.append(article.get_json())
        results = []
        for catalogue in catalogues:
            result = catalogue.get_json()
            result['articles'] = article_map.get(catalogue.id, [])
            results.append(result)
        return results

    @classmethod
    def move_a2c(cls, user_name, src, des):
        src_article = Article.select().get(src.get('id'))
        des_articles = Article.select().filter(
            Article.catalogue_id == des.get('id')
        ).all()
        articles = Article.select().filter(
            Article.catalogue_id == src_article.catalogue_id,
            Article.catalogue_index > src_article.catalogue_index
        ).all()
        for article in articles:
            article.catalogue_index -= 1
            article.update()
        src_article.catalogue_id = des.get('id')
        src_article.catalogue_index = 1
        src_article.update()
        for index, article in enumerate(des_articles):
            article.catalogue_index = index + 2
            article.update()

    @classmethod
    def move_c2c(cls, user_name, src, des):
        src_index = src.get('index')
        des_index = des.get('index')
        if src_index == des_index:
            return
        if src_index > des_index:  # 向上移动
            catalogues = Catalogue.select().filter(
                Catalogue.user_name == user_name,
                Catalogue.index.between(des_index, src_index)
            ).order_by(Catalogue.index.asc()).all()
            catalogues[-1].index = des_index
            catalogues[-1].update()
            for catalogue in catalogues[0: -1]:
                catalogue.index += 1
                catalogue.update()
        else:  # 向下移动
            catalogues = Catalogue.select().filter(
                Catalogue.user_name == user_name,
                Catalogue.index.between(src_index, des_index)
            ).order_by(Catalogue.index.asc()).all()
            for index, catalogue in enumerate(catalogues):
                if index == 0:
                    catalogue.index = des_index
                else:
                    catalogue.index -= 1
                catalogue.update()

    @classmethod
    def print_info(cls, articles):
        for article in articles:
            print(article.title, article.catalogue_id, article.catalogue_index)

    @classmethod
    def mov_a2a(cls, user_name, src, des):
        src_catalogue_id = src.get('catalogue_id')
        des_catalogue_id = des.get('catalogue_id')
        src_catalogue_index = src.get('catalogue_index')
        des_catalogue_index = des.get('catalogue_index')
        log.info(f'sid{src_catalogue_id}-sidx{src_catalogue_index}, did{des_catalogue_id}-didx{des_catalogue_index}')
        src_articles = Article.select().filter(
            Article.catalogue_id == src_catalogue_id
        ).order_by(Article.catalogue_index.asc()).all()
        des_articles = []
        if src_catalogue_id != des_catalogue_id:
            des_articles = Article.select().filter(
                Article.catalogue_id == des_catalogue_id
            ).order_by(Article.catalogue_index.asc()).all()
        src_article = src_articles[src_catalogue_index - 1]
        cls.print_info(src_articles)
        print('------')
        if src_catalogue_id == des_catalogue_id:
            src_articles.pop(src_catalogue_index - 1)
            if src_catalogue_index < des_catalogue_index:
                src_articles.insert(des_catalogue_index, src_article)
            else:
                src_articles.insert(des_catalogue_index - 1, src_article)
        else:
            article = src_articles.pop(src_catalogue_index - 1)
            article.catalogue_id = des_catalogue_id
            des_articles.insert(
                des_catalogue_index if src_catalogue_id < des_catalogue_id else des_catalogue_index - 1,
                src_article
            )
        cls.print_info(src_articles)
        for index, article in enumerate(src_articles):
            article.catalogue_index = index + 1
            article.update()
        for index, article in enumerate(des_articles):
            article.catalogue_index = index + 1
            article.update()

    @classmethod
    def move(cls, user_name, src, des):
        src_type = 'article' if src.get('catalogue_index', None) is not None else 'catalogue'
        des_type = 'article' if des.get('catalogue_index', None) is not None else 'catalogue'
        move_type = 'a2a'
        if src_type == 'article' and des_type == 'article':
            cls.mov_a2a(user_name, src, des)
        elif src_type == 'article' and des_type == 'catalogue':
            cls.move_a2c(user_name, src, des)
        elif src_type == 'catalogue' and des_type == 'catalogue':
            cls.move_c2c(user_name, src, des)
        return True

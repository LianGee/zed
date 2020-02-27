#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : qiniu_service.py
# @Author: zaoshu
# @Date  : 2020-02-12
# @Desc  :
import os

from qiniu import Auth, put_data, put_file, BucketManager, urlsafe_base64_decode

import config
from common.enc_util import md5
from common.exception import ServerException
from common.http_util import HttpUtil
from common.log import Logger

log = Logger(__name__)


class QiniuService:

    @classmethod
    def upload_img(cls, img, file_name=None, new_name=None):
        auth = Auth(config.QI_NIU.get('access_key'), config.QI_NIU.get('secret_key'))
        token = auth.upload_token(bucket=config.QI_NIU.get('img_bucket_name'))
        bucket = BucketManager(auth)
        if file_name is None:
            file_name = f'{md5(img)}'
        if new_name is None:
            new_name = file_name
        if len(img) >= 22 and img[0:22] == 'data:image/png;base64,':
            b64 = img.split(';base64,')[1]
            img = urlsafe_base64_decode(b64)
        file_stat = bucket.stat(bucket=config.QI_NIU.get('img_bucket_url'), key=file_name)
        delete_status = None
        if file_stat[0] is not None:
            delete_status = bucket.delete(bucket=config.QI_NIU.get('img_bucket_url'), key=file_name)
        if isinstance(delete_status, tuple) and delete_status[1].status_code != 200:
            raise ServerException(msg='更新图片失败')
        ret, res = put_data(token, key=new_name, data=img)
        return config.QI_NIU.get('img_bucket_url') + ret.get('key')

    @classmethod
    def get_img_info(cls, url):
        url = f'{url}?imageInfo'
        http_util = HttpUtil(
            url=url,
            method='GET'
        )
        return http_util.request().json()

    @classmethod
    def upload_doc(cls, data, file_name=None, new_name=None):
        auth = Auth(config.QI_NIU.get('access_key'), config.QI_NIU.get('secret_key'))
        token = auth.upload_token(bucket=config.QI_NIU.get('doc_bucket_name'))
        bucket = BucketManager(auth)
        if file_name is None:
            file_name = f'{md5(data)}'
            new_name = file_name
        delete_status = cls.delete_file(bucket_name=config.QI_NIU.get('doc_bucket_name'), file_name=file_name)
        if not delete_status:
            raise ServerException('更新文件失败')
        file_path = f'./data/{new_name}'
        f = open(file_path, 'wb')
        f.write(bytes(data, encoding='utf8'))
        f.close()
        ret, res = put_file(token, key=new_name, file_path=file_path, mime_type='text/plain')
        log.info(res)
        os.remove(file_path)
        return config.QI_NIU.get('doc_bucket_url') + ret.get('key')

    @classmethod
    def delete_file(cls, bucket_name, file_name):
        auth = Auth(config.QI_NIU.get('access_key'), config.QI_NIU.get('secret_key'))
        bucket = BucketManager(auth)
        file_stat = bucket.stat(bucket=bucket_name, key=file_name)
        delete_status = None
        if file_stat[0] is not None:
            delete_status = bucket.delete(bucket=bucket_name, key=file_name)
            log.info(f'delete file {file_name} from {bucket_name} with status {delete_status}')
        else:
            raise ServerException('文件不存在')
        if isinstance(delete_status, tuple) and delete_status[1].status_code != 200:
            return False
        return True

    @classmethod
    def get_doc(cls, url, summary=False):
        http_util = HttpUtil(
            url=url,
            headers={
                'Content-Type': 'text/plain'
            }
        )
        doc = http_util.request()
        text = doc.content.decode(encoding='utf8')
        if summary:
            return cls.get_summary(text)
        return text

    @classmethod
    def get_summary(cls, content):
        start = 100
        if len(content) > start:
            index = content[start: -1].find('\n')
            end = index if index == -1 else index + start
            return content[0: end]
        return content

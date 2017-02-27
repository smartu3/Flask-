#-*- coding:utf-8 -*-

#安装好Redis，并启动好redis服务，redis默认端口为6379
#pip install flask_cache

#配置cache并初始化
from flask import Flask
from flask_cache import Cache

cache = Cache()

config = {
	'CACHE_TYE':'redis',
	'CACHE_REDIS_HOST':'127.0.0.1',
	'CACHE_REDIS_PORT':6379,
	'CACHE_REDIS_DB':'',
	'CACHE_REDIS_PASSWORD':''
	}

app=Flask(__name__)
app.config.from_object(config)
cache.init_app(app)

@app.route('/')
@cache.cached(timeout=60*2)
def index():
	pass

#参考：http://www.pythondoc.com/flask-cache/#flask.ext.cache.Cache.memoize
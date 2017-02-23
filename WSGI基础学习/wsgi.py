# -*- coding:utf-8 -*-

# def app(environ,start_fn):
	# start_fn('200 OK',[('Content-Type','text/plain')])
	# return ['Hello World!\n']
#以上为最基本的Python Web应用：
#放在任何WSGI可编译服务器上运行，能得到HELLO WORLD 和200状态码

#一个最基本的WSGI应用是Python 可调用的，如函数，类，或者带有__call__方法的类实例
#可调用的应用接收两个参数，environ：一个包含必要数据的Python字典；start_fn，可调用的
#应用程序调用start_fn和两个参数：状态码，相关头部的列表，头部由元组组成
#应用程序返回包含bytes的可迭代对象
#若app是类，可以在__iter__方法里完成

# class app(object):
	# def __init__(self,environ,start_fn):
		# self.environ = environ
		# self.start_fn = start_fn
	# def __iter__(self):
		# self.start_fn('200 OK',[('Content-Type','text/plain')])
		# yield "Hello World!\n"

# class Application(object):
	# def __call__(self,environ,start_fn):
		# start_fn('200 OK',[('Content-Type','text/plain')])
		# yield "Hello World\n"
# app = Application()

#以上三例等效

#通过中间件能达到对应用程序的检查或者其他

# import pprint

# def handler(environ,start_fn):
	# start_fn('200 OK',[('Content-Type','text/plain')])
	# return ['Hello World\n']

# def log_environ(handler):
	# def _inner(environ,start_fn):
		# pprint.pprint(environ)
		# return handler(environ,start_fn)
	# return _inner

# app = log_environ(handler)

#也可以使用装饰器decorator

# from functools import wraps
# def log_decorator(f):
	# @warps(f)
	# def _inner(environ,start_fn):
		# pprint.pprint(environ)
		# return f(environ,start_fn)
	# return _inner

# @log_decorator
# def handler(environ,start_fn):
	# start_fn('200 OK',[('Content-Type','text/plain')])
	# return ['Hello World\n']

#使用装饰器能够让应用程序更优雅

from functools import wraps

def handler_error(f):
	@wraps(f)
	def _inner(environ,start_fn):
		try:
			return f(environ,start_fn)
		except Exception as e:
			print e
			start_fn('500 Server Error',[('Content-Type','text/plain')])
			return ['500 Server Error']
	return _inner

def wrap_query_params(f):
	@wraps(f)
	def _inner(environ,start_fn):
		qs = environ.get('QUERY_STRING')
		environ['QUERY_STRING_PARAMS'] = urlparse.parse_qs(qs)
		return f(environ,start_fn)
	return _inner

@handler_error
@wrap_query_params
def handler(environ,start_fn):
	 start_fn('200 OK',[('Content-Type','text/plain')])
	 return ['Hello World\n']

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:13:19 2018

@author: lenovo
"""

from flask import Flask
app = Flask(__name__)

'''
@app.route('/')
def hello_world():
    return 'Hello World!'
'''

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
'''
int	接受整数
float	同 int ，但是接受浮点数
path	和默认的相似，但也接受斜线
'''
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

'''
它们结尾斜线的使用在 URL 定义 中不同。 
第一种情况中，指向 projects 的规范 URL 尾端有一个斜线。像在文件系统中的文件夹。访问一个结尾不带斜线的 URL 会被 Flask 重定向到带斜线的规范 URL 去。
第二种情况的 URL 结尾不带斜线，类似 UNIX-like 系统下的文件的路径名。访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误。
这个行为使得在遗忘尾斜线时，允许关联的 URL 接任工作，与 Apache 和其它的服务器的行为并无二异。
此外，也保证了 URL 的唯一，有助于避免搜索引擎索引同一个页面两次。
'''
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.debug = True
    app.run()
    
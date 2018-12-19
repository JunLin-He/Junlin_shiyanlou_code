#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    # 显示文章名称的列表
    # 页面中需要显示 `/home/shiyanlou/files/` 目录下所有 json 文件中的 `title` 信息列表
    title_list = []
    with open('/Users/junlinhe/Documents/Code_lib/python_challenge/week_two_homewrok/files/helloshiyanlou.json', 'r') as file1:
        json_file1 = json.loads(file1.read())
        title_list.append(json_file1['title'])
    with open('/Users/junlinhe/Documents/Code_lib/python_challenge/week_two_homewrok/files/helloworld.json', 'r') as file2:
        json_file2 = json.loads(file2.read())
        title_list.append(json_file2['title'])
    return render_template('index.html', title_list=title_list)

@app.route('/files/<filename>')
def file(filename):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='hellshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面
    filename = filename + '.json'
    path = os.listdir("/Users/junlinhe/Documents/Code_lib/python_challenge/week_two_homewrok/files")
    if filename in path:
        # 将json文件转换为python字典对象
        with open('/Users/junlinhe/Documents/Code_lib/python_challenge/week_two_homewrok/files/' + filename, 'r') as file:
            json_file = json.loads(file.read())        
        return render_template('file.html', json_file=json_file)
    else:
        return render_template('404.tml'), 404

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    # 如果在终端直接用flask run执行，以下代码是不会运行的，因为此时__name__并不等于__main__
    # 所以如果想设置运行的host和port，最好使用命令行参数 flask run -h '0.0.0.0' -p 3000
    app.run(host='127.0.0.1', port=3000, debug=True)



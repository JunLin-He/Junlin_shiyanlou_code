"""
请完成一个应用，当 URL 是http://127.0.0.1/sum/a/b时，其中a和b都是数字，服务器返回它们的和。
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    return str(a+b)

if __name__ == '__main__':
    app.run()
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/shiyanlou')
def shiyanlou():
    return 'River!'

if __name__ == '__main__':
    app.run()
from flask import Flask
app = Flask(__name__)

#最簡單的方式
# @app.route('/')
# def hello_world():
#    return 'Hello World 12345'

#url 指往function
# http://127.0.0.1:5000/hello
# @app.route('/hello')
# def hello_world():
#    return 'first project'

# 這個方式怪怪的
def hello_world():
   return 'first project'
app.add_url_rule('/test', '', hello_world)

if __name__ == '__main__':
   app.run()
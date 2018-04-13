# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/hello/<name>')
# def hello(name):
#    return 'Hello %s!' % name
#
# if __name__ == '__main__':
#    app.run(debug = True)

# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#    return 'Blog Number %d' % postID
#
# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#    return 'Revision Number %f' % revNo
#
# if __name__ == '__main__':
#    app.run()


from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run(port=8000)
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def result():
   if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
        print(username)
        print(password)
        # return ('GET %s $s' %(str(username),str(password)))
        return ('GET ')


if __name__ == '__main__':
   app.run(debug = True,port=8000)
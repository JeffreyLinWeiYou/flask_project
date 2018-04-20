from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'asus#1234'
app.config['MYSQL_DATABASE_DB'] = 'SimpleMySQL'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

api = Api(app)

class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _userName = args['username']
            _userPassword = args['password']

            conn = mysql.connect()
            cursor = conn.cursor()

            # INSERT
            # INTO
            # Store_Information(Store_Name, Sales, Txn_Date)
            # VALUES('Los Angeles', 900, 'Jan-10-1999');
            cursor.execute('INSERT INTO UserData(username,password) VALUES("{}","{}")'.format(_userName,_userPassword))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'User creation success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}

    def get(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _userName = args['username']
            _userPassword = args['password']

            conn = mysql.connect()
            cursor = conn.cursor()

            # INSERT
            # INTO
            # Store_Information(Store_Name, Sales, Txn_Date)
            # VALUES('Los Angeles', 900, 'Jan-10-1999');
            cursor.execute('INSERT INTO UserData(username,password) VALUES("{}","{}")'.format(_userName,_userPassword))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'User creation success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}

class UpdateUser(Resource):
    def put(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _userName = args['username']
            _userPassword = args['password']

            conn = mysql.connect()
            cursor = conn.cursor()
            # UPDATE
            # "表格名"
            # SET
            # "欄位1" = [新值]
            # WHERE
            # "條件";

            cursor.execute('UPDATE UserData SET password = "{}" WHERE username = "{}"'.format(_userPassword,_userName))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'User update success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}

class DeleteUser(Resource):
    def delete(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str, help='id')
            args = parser.parse_args()

            _userId = args['id']

            conn = mysql.connect()
            cursor = conn.cursor()
            # DELETE
            # FROM
            # "表格名"
            # WHERE
            # "條件";

            cursor.execute('DELETE FROM UserData WHERE idUserData = {}'.format(_userId))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'User delete success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/CreateUser')
api.add_resource(UpdateUser, '/UpdateUser')
api.add_resource(DeleteUser, '/DeleteUser')



if __name__ == '__main__':
    app.run(debug=True,port=5001)
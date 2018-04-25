
from home.main.model import Users
from home.db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'extra': fields.String,
}

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('name', type=str)
parser.add_argument('extra', type=str)


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        parsed_args = parser.parse_args()
        message = session.query(Users).filter(Users.id == parsed_args['id']).first()
        if not message:
            abort(404, message="User {} doesn't exist".format(id))
        return message

    @marshal_with(user_fields)
    def post(self):
        parsed_args = parser.parse_args()
        user = Users(name=parsed_args['name'],extra=parsed_args['extra'])

        session.add(user)
        session.commit()
        return user, 201

    def delete(self):
        parsed_args = parser.parse_args()
        message = session.query(Users).filter(Users.id == parsed_args['id']).first()
        if not message:
            abort(404, message="User {} doesn't exist".format(id))
        session.delete(message)
        session.commit()
        return {}, 204

    @marshal_with(user_fields)
    def put(self):
        parsed_args = parser.parse_args()
        user = session.query(Users).filter(Users.id == parsed_args['id']).first()
        user.name = parsed_args['name']
        user.extra = parsed_args['extra']

        session.commit()
        return user, 201

class UserResourceList(Resource):
    @marshal_with(user_fields)
    def get(self):
        user = session.query(Users).all()
        return user

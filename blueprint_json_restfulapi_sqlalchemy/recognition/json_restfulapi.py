# -*- coding: utf-8 -*-

from recognition.model import Recognition
from db import session

from flask_restful import reqparse
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with
import json


response_fields = {
    'id': fields.Integer,
    'type': fields.Integer,
    'resultIdx': fields.String,
    'time': fields.Integer,
    'dbId': fields.String,
    'score': fields.String,
    'user_idx': fields.String,
}

parser = reqparse.RequestParser()
parser.add_argument('response', type=str)


class ResponseResource(Resource):

    @marshal_with(response_fields)
    def post(self):
        parsed_args = parser.parse_args()
        json_data = parsed_args['response']
        data = json.loads(json_data)

        response = Recognition(type=data['type'],resultIdx=data['resultIdx'],time=data['recogResult']['time'],
                         dbId=data['recogResult']['similars'][0]['dbId'],score=data['recogResult']['similars'][0]['users'][0]['score'],
                         user_idx=data['recogResult']['similars'][0]['users'][0]['user_idx']
                         )

        session.add(response)
        session.commit()
        return response, 201


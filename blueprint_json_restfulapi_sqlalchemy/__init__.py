# -*- coding: utf-8 -*-

from app import app
from management import user_restful
from management.model import user_model
from recognition.model import recognition_model
from recognition import json_restfulapi

from flask_restful import Api


api = Api(app)


app.register_blueprint(management, url_prefix='/')
app.register_blueprint(user_model)

app.register_blueprint(recognition_model)


api.add_resource(user_restful.UserResource, '/user_restful')
api.add_resource(user_restful.UserResourceList, '/user_restful_list')

api.add_resource(json_restfulapi.ResponseResource, '/response')

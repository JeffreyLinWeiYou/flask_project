# -*- coding: utf-8 -*-

from flask import Flask
from blueprints.management.views import management
from blueprints.management import user_restful
from blueprints.management.model import user_model
from blueprints.recognition.model import recognition_model
from blueprints.recognition import json_restfulapi

from flask_restful import Api


app = Flask(__name__)
api = Api(app)


app.register_blueprint(management, url_prefix='/')
app.register_blueprint(user_model)

app.register_blueprint(recognition_model)


api.add_resource(user_restful.UserResource, '/user_restful')
api.add_resource(user_restful.UserResourceList, '/user_restful_list')

api.add_resource(json_restfulapi.ResponseResource,'/response')

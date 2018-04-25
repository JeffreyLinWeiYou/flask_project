from flask import Flask
from home.main.views import main

from home.main import user_restful

from home.main.model import user_model

from flask_restful import Api


app = Flask(__name__)
api = Api(app)


app.register_blueprint(main, url_prefix='/')

app.register_blueprint(user_model)

api.add_resource(user_restful.UserResource, '/user_restful')
api.add_resource(user_restful.UserResourceList, '/user_restful_list')

from flask import Flask
from home.main.controller import main
from home.admin.controller import admin

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
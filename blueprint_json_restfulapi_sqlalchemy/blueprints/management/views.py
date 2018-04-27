# -*- coding: utf-8 -*-

from flask import Blueprint, render_template


management = Blueprint('management', __name__,template_folder='templates')

@management.route('/')
def index():
    return render_template('index.html')




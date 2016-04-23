from flask import Flask

app = Flask(__name__)
#SESSION_TYPE = 'mongodb'

from app import views
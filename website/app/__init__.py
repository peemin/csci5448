import os
from flask import Flask
import pymongo
from pymongo import MongoClient

# Specify the database
app = Flask(__name__)
#SESSION_TYPE = 'mongodb'

from app import views
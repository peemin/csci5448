from flask import Flask

#Creates a flask object app to run the program
app = Flask(__name__)

#imports the views.py file
from app import views
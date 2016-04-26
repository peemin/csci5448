#!flask/bin/python

#This code pulls the init.py file from the app folder to run the website
import os 

from app import app

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
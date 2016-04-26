This is the final project of Peemin Chen and Margaret Wheeler for CSCI 5448. This repo contains code for our application using python. Other modules and languages used were Bootstrap, Jinja2, Flask, and MongoDB(using Pymongo).

**App Demo**

The code for our project was uploaded to our Heroku cloud platform. If you would like to see how it works, a demo of the project can be found here: 

[https://grocerylist.herokuapp.com/](https://grocerylist.herokuapp.com/)

If you would like to run this project locally on your machine, you will need to install Flask, MongoDB, and Pymongo. Please use Python 2 to compile and run files. Links to installation instructions can be found below. 

**Download Instruction Links**

Flask: [http://flask.pocoo.org/docs/0.10/installation/](http://flask.pocoo.org/docs/0.10/installation/)

MongoDB: [https://docs.mongodb.org/manual/installation/](https://docs.mongodb.org/manual/installation/)

Pymongo: [https://api.mongodb.org/python/current/installation.html](https://api.mongodb.org/python/current/installation.html)

**Instructions for Running Program**

You will also need to go into website/run.py and website/lib/dbController.py and uncomment/comment out code as instructed in the individual files.

After doing all of this, you must do the following. 

Open the website folder
Open cmd or terminal and run the following 

**Linux/OSX:** 

```mongod --dbpath data```

**Windows:**

```C:\mongodb\bin\mongod.exe --dbpath data```

In a separate terminal or cmd window, run

**MacOSX/Linux**

```python run.py```

**Windows**

```py run.py```

If run correctly, the output should give you a local IP http://127.0.0.1:5000/ or some varint that you can load into a web browser and view the website. 

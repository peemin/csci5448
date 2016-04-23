import unittest
from datetime import datetime

from user import User

uname = 'Magic1@unicorn.com'
password = 'superpanda'

user = User(uname, password)
user.setName('Awesome Unicorn')

glist0 = {"items":['spinach, 1 bunch','corn, 4 can'],"gname":"grocery list 1"}
glist1 = {"items":['broccli, 1 bunch','peas, 2 bag'],"gname":"grocery list 2"}
glist2 = {"items":['chicken, 1 whole','corn, 4 can'],"gname":"grocery list 3"}
glist3 = {"items":['carrot, 1 bunch','peas, 2 bag'],"gname":"grocery list 4"}
glists = [glist0,glist1,glist2,glist3]

user.updateGLists(glists)
print(user.getName())
print("Grocery Lists")
print(user.getGLists())


from grocery import GroceryLists
from user import User 

user = 'Magic1@unicorn.com'
groceryLists = GroceryLists(user)
glists = groceryLists.getLists()

print(glists[0])



#glists = db.getGLists("Magic1@unicorn.com)
from dbController import MongodbController
from grocery import GroceryLists

class User(object):
    def __init__(self,email,password):
        self.db = MongodbController()
        self.user = email
        self.password = password
        self.name = email
        
        self.glistController = GroceryLists(self.user)
        self.groceryLists = None
        self.__setGlists()  # set grocery list from the database
        
        self.currentListIndex = 0
    
    def exist(self):
        if self.db.getUser(self.user) is None: return False
        self.name = self.db.getName(self.user)
        return True
    
    def login(self):
        return self.db.login(self.user,self.password)
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.db.upateName(self.user, name)
        self.name = self.db.getName(self.user)
    
    def getPassword(self):
        return self.password
    
    def setPassword(self,password):
        self.password = password
        self.db.upatePassword(self.user, password)
        self.password = self.db.getPassword(self.user)
    
    # returns a dictionary of all the grocery lists
    def getGLists(self):
        return self.groceryLists
    
    # private method for User class
    # gets grocery lists from the database
    def __setGlists(self):
        self.groceryLists = self.glistController.getLists()
    
    def updateGLists(self, glists):
        self.glistController.updateLists(glists)
        self.__setGlists()
        if self.groceryLists == glists:
            return True
        else:
            return False
    
    def deleteGLists(self):
        self.glistController.deleteLists()
        self.__setGlists()
        if self.groceryLists is None:
            return True
        else:
            return False
        
    def getCurrentListIndex(self): 
        return self.currentListIndex
    
    def updateCurrentListIndex(self, newlistIndex):
        self.currentList = newlistIndex 

    def getCurrentGList(self):
        print ("Get Current Grocery List")
        glist = self.groceryLists[self.currentListIndex]["items"]
        return glist
    
    def getCurrentGlistName(self):
        return self.groceryLists[self.currentListIndex]["gname"]
        
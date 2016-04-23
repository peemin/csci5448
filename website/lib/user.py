from dbController import MongodbController
from grocery import GroceryLists

class User(object):
    def __init__(self,email,password):
        self.db = MongodbController()
        self.user = email
        self.password = password
        self.name = email
        
        self.glistController = GroceryLists(self.user)
 
        self.currentListIndex = 0

    def getCurrentListIndex(self): 
        return self.currentListIndex
    
    def updateCurrentListIndex(self, newlistIndex):
        self.currentListIndex = newlistIndex
    
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
        return self.glistController.getLists()
            
    def getGListsNames(self):
        return self.glistController.getGroceryListNames()
    
    def getGListsItemList(self):
        return self.glistController.getGroceryItemsList()

    def updateGLists(self, glists):
        self.glistController.updateLists(glists)
        
        if self.getGLists() == glists:    
            return True
        else:
            return False
    
    def deleteGLists(self):
        self.glistController.deleteLists()
        if self.getGLists() is None:
            return True
        else:
            return False
        
    def getCurrentGList(self):
        glist = self.getGLists()[self.currentListIndex]["items"]
        return glist
    
    def getCurrentGlistName(self):
        return self.getGLists()[self.currentListIndex]["gname"]
    
    def addNewGroceryList(self, gname, item):
        glist = self.getGLists() + [{"gname":gname,"items":[item]}]
        self.updateGLists(glist)
        
    def addNewCurrentListItem(self,item):
        glists = self.getGLists()
        glists[self.currentListIndex]["items"].append(item)
        self.updateGLists(glists)


        
    
        

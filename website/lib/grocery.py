from applist import Applist
class GroceryLists(Applist):
    def __init__(self,user):
        super(GroceryLists, self).__init__(user)

    def getLists(self):
        return self.db.getGLists(self.user)
    
    def updateLists(self,glists):
        self.db.updateGLists(self.user, glists)
    
    def deleteLists(self):
        self.db.deleteGLists(self.user)
           
        
            
        
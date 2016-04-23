from applist import Applist
class PantryLists(Applist):
    def __init__(self,user):
        super().__init__(user)

    def getLists(self):
        return self.db.getPLists(self.user)
    
    def updateLists(self,plists):
        self.db.updatepLists(self.user, plists)
    
    def deleteLists(self):
        self.db.deletePLists(self.user)
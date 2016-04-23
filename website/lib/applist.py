import abc
from dbController import MongodbController
class Applist(object):
    
    @abc.abstractmethod
    def __init__(self,user):
        # child __init__ method needs to call this parent __init__ to configure db
        self.db = MongodbController()
        self.user = user
          
    @abc.abstractmethod
    def getLists(self):
        raise NotImplementedError()
        
    @abc.abstractmethod
    def updateLists(self,applists):
        raise NotImplementedError()
        
    @abc.abstractmethod
    def deleteLists(self):
        raise NotImplementedError()
 
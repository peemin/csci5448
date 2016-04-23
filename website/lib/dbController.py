from pymongo import MongoClient
from datetime import datetime

class  MongodbController(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.grocery

    def getUser(self, uname):
        return self.db.users.find_one({'user': uname})
    
    def addUser(self, uname, password):
        if self.db.users.find_one({'user': uname}) is None:
            post = {'user': uname,'password': password, 'name':uname}
            self.db.users.insert_one(post)
            return True
        else:
            return False
    
    def deleteUser(self, uname):
        result = self.db.users.delete_many({'user': uname})
        if result.deleted_count > 0:
            return True
        else:
            return False
        
    def login(self, uname, password):
        if self.db.users.find_one({'user': uname,'password': password}) is None:
            return False
        else:
            return True
        
    def upatePassword(self, uname, password):
        user = self.db.users.find_one({'user': uname})
        if user is None:
            return False
        else:
            self.db.users.update_one({'user':uname},{'$set':{'password':password}})
            return True
    def getPassword(self, uname):
        user = self.db.users.find_one({'user': uname})
        return user['password']
    
    def upateName(self, uname, name):
        user = self.db.users.find_one({'user': uname})
        if user is None:
            return False
        else:
            self.db.users.update_one({'user':uname},{'$set':{'name':name}})
            return True
    
    def getName(self, uname):
        user = self.db.users.find_one({'user': uname})
        return user['name']
   
    def insertGLists(self, uname, glists):
        self.db.glists.insert_one({'user':uname,'glists':glists})
        
    def updateGLists(self, uname, glists):
        self.db.glists.update_one({'user':uname},
                                  {'$set':{'glists':glists}},
                                  upsert = True)
        
    def getGLists(self,uname):
        result = self.db.glists.find_one({'user': uname})
        if result is None:
            return None
        return result['glists']
    
    def deleteGLists(self, uname):
        result = self.db.glists.delete_many({'user': uname})
        if result.deleted_count > 0:
            return True
        else:
            return False
        
    def getPLists(self, uname):
        result = self.db.plists.find_one({'user': uname})
        if result is None:
            return result
        return result['plists']
    
    def updatepLists(self, uname, plists):
        self.db.plists.update_one({'user':uname},
                                  {'$set':{'plists':plists}},
                                  upsert = True)

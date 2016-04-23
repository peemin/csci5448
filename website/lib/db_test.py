import unittest
from dbController import MongodbController

class MongoDBTest(unittest.TestCase):
    def setUp(self):
        self.db = MongodbController()
        
    def test_addDeleteUser(self):
        uname = 'steve1'
        password = 'password1'
        self.db.deleteUser(uname)
        self.assertIs(self.db.addUser(uname,password), True)
        self.assertIs(self.db.addUser(uname,password), False)
        self.assertIs(self.db.deleteUser(uname), True)

    def test_loginUser(self):
        uname = 'peemin'
        password = 'yippy'
        self.db.deleteUser(uname)
        self.assertIs(self.db.login(uname,password), False)
        self.db.addUser(uname,password)
        self.assertIs(self.db.login(uname,password), True)
        self.db.deleteUser(uname)
        
    def test_updateName(self):
        uname = 'wheel'
        password = 'pinkmonkey'
        name = 'Margaret'
        self.db.deleteUser(uname)
        self.db.addUser(uname,password)
        self.assertIs(self.db.upateName(uname,name), True)
        self.assertIs(self.db.upateName('peemin','punk'), False)
        self.db.deleteUser(uname)
    
    def test_updatePassword(self):
        uname = 'wheel'
        password = 'pinkmonkey'
        newPW = 'clown123'
        self.db.deleteUser(uname)
        self.db.addUser(uname,password)
        self.assertIs(self.db.upatePassword(uname,newPW), True)
        self.assertIs(self.db.upatePassword('peemin','punk'), False)
        self.db.deleteUser(uname)
      
    def test_getUser(self):
        uname = 'clown@colorado.edu'
        password = 'clown123'
        name = 'Master Mind'
        self.db.deleteUser(uname)
        self.db.addUser(uname,password)
        self.db.upateName(uname,name)
        user = self.db.getUser(uname)
        self.assertEqual(user['user'], uname)
        self.assertEqual(user['password'], password)
        self.assertEqual(user['name'], name)
        self.db.deleteUser(uname)
        self.assertIsNone(self.db.getUser(uname))
        
    def test_glists(self):
        uname = 'glistuser'
        password = 'p123'
        
        self.db.deleteUser(uname)
        self.db.deleteGLists(uname)
        user = self.db.getUser(uname)
        
        glist1 = {"items":['spinach, 1 bunch','corn, 4 can'],"gname":"grocery list 1"}
        glist2 = {"itmes":['broccli, 1 bunch','peas, 2 bag'],"gname":"grocery list 2"}
        glists = [glist1,glist2]
        
        glist3 = {"items":['chicken, 1 whole','corn, 4 can'],"gname":"grocery list 3"}
        glist4 = {"items":['carrot, 1 bunch','peas, 2 bag'],"gname":"grocery list 4"}
        
        glists2 = [glist3, glist4]
        
        if user is None:
            self.db.addUser(uname,password)
        
        userglists = self.db.getGLists(uname)
        
        if userglists is None:
            print ('glists is none')

            self.db.updateGLists(uname,glists)
            userglists = self.db.getGLists(uname)
            self.assertIsNotNone(userglists)
            print (userglists)
        

        self.db.updateGLists(uname,glists2)
        userglists2 = self.db.getGLists(uname)
        print ("in test_glists")
        print (userglists2)
        
        self.assertEqual(userglists2[0]["items"][1],glist3["items"][1])
        
        self.db.deleteUser(uname)
        self.db.deleteGLists(uname)

     
if __name__ == '__main__':
    unittest.main()
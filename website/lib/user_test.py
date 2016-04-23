import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.glist0 = {"items":['spinach, 1 bunch','corn, 4 can'],"gname":"grocery list 1"}
        self.glist1 = {"items":['broccli, 1 bunch','peas, 2 bag'],"gname":"grocery list 2"}
        self.glist2 = {"items":['chicken, 1 whole','corn, 4 can'],"gname":"grocery list 3"}
        self.glist3 = {"items":['carrot, 1 bunch','peas, 2 bag'],"gname":"grocery list 4"}
        self.glists = [self.glist0,self.glist1,self.glist2,self.glist3]
        
        self.name1 = 'Magic1@unicorn.com'
        self.password1 = 'superpanda'
        self.user1 = User(self.name1,self.password1)
        self.user1.updateGLists(self.glists)
        
        self.name2 = 'DoesNotExist'
        self.password2 = 'DoesNotExist'
        self.user2 = User(self.name2,self.password2)
    
    def test_userExist(self):
        self.assertTrue(self.user1.exist())
    
    def test_userDoesNotExist(self):
        self.assertFalse(self.user2.exist())
    
    def test_canLogin(self):
        self.assertTrue(self.user1.login())
        
    def test_canNotLogin(self):
        self.assertFalse(self.user2.login())
                
    def test_getName(self):
        self.assertEqual(self.user2.getName(),self.name2)
        
    def test_setName(self):    
        newName = 'Maggy'
        self.user1.setName(newName)
        self.assertEqual(self.user1.getName(),newName)
        self.user1.setName(self.name1)
        
    def test_getGroceryLists(self):
        result = self.user1.getGLists()
        self.assertIsNotNone(result)
        self.user2.deleteGLists()
        self.assertIsNone(self.user2.getGLists())
                
    def test_updateGroceryLists(self):
        
        self.assertTrue(self.user2.updateGLists(self.glists))
        result = self.user2.getGLists()
        self.assertEqual(result[0]["gname"],self.glist0["gname"])
        self.user2.deleteGLists()
        
      
    def test_getCurrentGList(self):
        self.user1.updateCurrentList(1)
        self.assertEqual(self.user1.getCurrentGList(),self.glist1["items"])
    
    def test_getCurrentGlistName(self):
        self.user1.updateCurrentList(3)
        self.assertEqual(self.user1.getCurrentGlistName(),self.glist3["gname"])
        
        
if __name__ == '__main__':
    unittest.main()
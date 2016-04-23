import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.glistNames = ["grocery list 1","grocery list 2","grocery list 3","grocery list 4"]
        self.itemsList = [['spinach, 1 bunch','corn, 4 can'],['broccli, 1 bunch','peas, 2 bag'],
                          ['chicken, 1 whole','corn, 4 can'],['carrot, 1 bunch','peas, 2 bag']]
        self.glist0 = {"items":self.itemsList[0],"gname":self.glistNames[0]}
        self.glist1 = {"items":self.itemsList[1],"gname":self.glistNames[1]}
        self.glist2 = {"items":self.itemsList[2],"gname":self.glistNames[2]}
        self.glist3 = {"items":self.itemsList[3],"gname":self.glistNames[3]}
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
        print ("\n test_getGroceryLists:")
        print (result)
                
    def test_updateGroceryLists(self):
        
        self.assertTrue(self.user2.updateGLists(self.glists))
        result = self.user2.getGLists()
        self.assertEqual(result[0]["gname"],self.glist0["gname"])
        self.user2.deleteGLists()
        
      
    def test_getCurrentGList(self):
        self.user1.updateCurrentListIndex(1)
        self.assertEqual(self.user1.getCurrentGList(),self.glist1["items"])
    
    def test_getCurrentGlistName(self):
        self.user1.updateCurrentListIndex(3)
        self.assertEqual(self.user1.getCurrentGlistName(),self.glist3["gname"])
        
    def test_getGListsNames(self):        
        result = self.user1.getGListsNames()
        self.assertEqual(result,self.glistNames)
        print("\n test_getGListsNames:")
        print (result)
        
    def test_getGListsItemList(self):        
        result = self.user1.getGListsItemList()
        self.assertEqual(result,self.itemsList)
        print("\ntest_getGListsItemList")
        print (result)  
        
    def test_addNewGroceryList(self):
        gname = "New Item List"
        self.user1.addNewGroceryList(gname)
        result = self.user1.getGListsNames()
        self.assertEqual(result[-1],gname)
        gl = self.user1.getGLists()
        self.user1.updateGLists(self.glists)
        print("\n test_addNewGroceryList:")
        print (gl)
        
    def test_addNewCurrentListItem(self):
        item = 'olives, 10 can'
        self.user1.addNewCurrentListItem(item)
        result = self.user1.getCurrentGList()
        self.assertEqual(result[-1],item)
        print("\n test_addNewCurrentListItem:")
        print(self.user1.getGLists())
        print("\n\n")
        print(result)
        
if __name__ == '__main__':
    unittest.main()

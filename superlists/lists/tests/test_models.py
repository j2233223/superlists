from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List



class ListAndItemModelTest(TestCase):


    def test_可以儲存及取出清單項目(self):
        list_ = List()
        list_.save()
        
        firstItem = Item()
        firstItem.text = '第一個清單項目'
        firstItem.list = list_
        firstItem.save()
        
        secondItem = Item()
        secondItem.text = '第二個清單項目'
        secondItem.list = list_
        secondItem.save()

        savedList = List.objects.first()
        self.assertEqual(savedList, list_)    
                
        savedItems = Item.objects.all()
        self.assertEqual(savedItems.count(), 2)    
        
        firstSavedItem = savedItems[0]
        secondSavedItem = savedItems[1]
        self.assertEqual(firstSavedItem.text, '第一個清單項目')
        self.assertEqual(firstSavedItem.list, list_)
        self.assertEqual(secondSavedItem.text, '第二個清單項目')
        self.assertEqual(secondSavedItem.list, list_)


    def test_不能儲存空的清單項目(self):
        list_ = List.objects.create()
        item = Item(text='', list=list_)
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()
        
        
        
        
        
        
          
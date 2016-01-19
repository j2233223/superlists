from django.http import HttpRequest
from django.shortcuts import render
from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import homePage
from selenium.webdriver.common.keys import Keys
from lists.models import Item
# Create your tests here.

class HomePageTest(TestCase):


    def test_root_url_resolves_to_homePage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homePage)


    def test_homePage可以POST請求(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['itemText'] = '新的項目'
        homePage(request)
        
        self.assertEqual(Item.objects.count(), 1)
        newItem = Item.objects.first()
        self.assertEqual(newItem.text, '新的項目')
        
        
    def test_homePage在POST之後轉址(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['itemText'] = '新的項目'
        response = homePage(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
        
        
    def test_homePage只在必要時儲存項目(self):
        request = HttpRequest()
        homePage(request)
        self.assertEqual(Item.objects.count(), 0)
     
     
    def test_homePage顯示出所有項目(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        
        request = HttpRequest()
        response = homePage(request)
        if response:
            response = response.content.decode('UTF-8')
        
        self.assertIn('itemey 1', response)
        self.assertIn('itemey 2', response)
                   
class ItemModelTest(TestCase):
    
    
    def test_儲存及提取項目(self):
        firstItem = Item()
        firstItem.text = '第一個清單項目'
        firstItem.save()
        
        secondItem = Item()
        secondItem.text = '第二個清單項目'
        secondItem.save()    
        
        savedItems = Item.objects.all()
        self.assertEqual(savedItems.count(), 2)
        
        firstSavedItem = savedItems[0]
        secondSavedItem = savedItems[1]
        self.assertEqual(firstSavedItem.text, '第一個清單項目')
        self.assertEqual(secondSavedItem.text, '第二個清單項目')


class ListViewTest(TestCase):
    
    def test_顯示所有項目(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
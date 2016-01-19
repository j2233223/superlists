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
        response = homePage(request)
        if response:
            response = response.content.decode('UTF-8')
        expectedHTML = render(request, 'lists/home.html')
        self.assertIn('新的項目', response)
        expectedHTML = render(request, 'lists/home.html', {'itemText':'新的項目'})
        if expectedHTML:
            expectedHTML = expectedHTML.content.decode('UTF-8')
        self.assertEqual(response, expectedHTML)
        
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

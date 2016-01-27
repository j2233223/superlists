from django.core.urlresolvers import resolve, reverse
from django.http import HttpRequest
from django.shortcuts import render
from django.test import TestCase
from selenium.webdriver.common.keys import Keys

from lists.models import Item, List 
from lists.views import homePage


# Create your tests here.
class HomePageTest(TestCase):


    def test_root_url_resolves_to_homePage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homePage)

                   
class ListViewTest(TestCase):

    def test_use_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(reverse('lists:viewList', args=(list_.id,)))
        self.assertTemplateUsed(response, 'lists/list.html')
        
    
    def test_displays_only_items_for_that_list(self):
        correctList = List.objects.create() 
        Item.objects.create(text='itemey 1', list=correctList)
        Item.objects.create(text='itemey 2', list=correctList)
        otherList = List.objects.create()
        Item.objects.create(text='other list item 1', list=otherList)
        Item.objects.create(text='other list item 2', list=otherList) 
        response = self.client.get(reverse('lists:viewList', args=(correctList.id,))) 
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2') 
        
class NewListTest(TestCase):


    def test_saving_a_POST_request(self):
        self.client.post(reverse('lists:newList'), data={'itemText':'新的項目'})
        self.assertEqual(Item.objects.count(), 1)
        newItem = Item.objects.first()
        self.assertEqual(newItem.text, '新的項目')


    def test_redirect_after_POST(self):
        response = self.client.post(reverse('lists:newList'), data={'itemText':'新的項目'})
        newList = List.objects.first()
        self.assertRedirects(response, reverse('lists:viewList', args=(newList.id,)))
        


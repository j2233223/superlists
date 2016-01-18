from django.shortcuts import render
from django.http import HttpResponse 


def homePage(request):
    return HttpResponse('<!doctype html><html><head>\
<title>待辦事項清單</title></head><body></body></html>')
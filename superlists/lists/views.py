from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from lists.models import Item, List
from django.core.exceptions import ValidationError
from django.utils.html import escape

# Create your views here.
def homePage(request):
    return render(request, 'lists/home.html')


def viewList(request, listID):
    list_ = List.objects.get(id=listID)    
    return render(request, 'lists/list.html', {'list':list_})


def newList(request):
    list_ = List.objects.create()
    item = Item(text=request.POST.get('itemText'), list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = escape('清單項目不能空白')
        return render(request, 'lists/home.html', {'error':error})
    return redirect(reverse('lists:viewList', args=(list_.id, )))

def addItem(request, listID):
    list_ = List.objects.get(id=listID)
    Item.objects.create(text=request.POST['itemText'], list=list_)
    return redirect(reverse('lists:viewList', args=(list_.id, )))
from django.shortcuts import render


def homePage(request):
    context = {'itemText':request.POST.get('itemText')}
    return render(request, 'lists/home.html', context)
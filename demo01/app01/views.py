from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        print(request.POST)
        # <QueryDict: {'user': ['zz'], 'pwd': ['123']}>
        print(request.body)
        # b'name=zz&password=123'
        print(request.data)
        return HttpResponse('ok')

from django.http import HttpResponse
from django.shortcuts import render


def fun(request,info):
    return HttpResponse("<h1>{}</h1>".format(info))

def template(request):
    d={'data':{'a':1,'b':2}}
    return render(request,'hai.html',context=d)
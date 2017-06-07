from django.shortcuts import render
from django.http import HttpResponse
from webGenApp.models import Person, Show

def index(request):
    context_dict={"key1":"thisthatandtheother","key2":"me and you"}
    return render(request,'webGenApp/index.html',context=context_dict)

def test(request,capture):
        qs=Person.objects.filter(firstName=capture).values()

        return render(request,'webGenApp/test.html',context=qs[0])

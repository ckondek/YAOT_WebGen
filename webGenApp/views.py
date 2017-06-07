from django.shortcuts import render
from django.http import HttpResponse
from webGenApp.models import Person, Show

def index(request):
    qs=Person.objects.all()
    markup='<ul>'
    for item in qs:
        markup +='<li><a href='+item.firstName+' '+item.lastName+'/a></li>'
    markup+='</ul>'
    return HttpResponse(markup)

def test(request,capture):
        qs=Person.objects.filter(firstName=capture).values()

        return render(request,'webGenApp/test.html',context=qs[0])

from django.shortcuts import render
from django.http import HttpResponse
from webGenApp.models import Person, Show

def index1(request,capture):
    qs=Person.objects.filter(show_id=capture).values()
    markup= '<p style="margin-left:50px;">... database initialization ...</p>'
    markup+='<div style="width:1000px;margin-left: 50px;">'
    markup+='<ul >'
    for item in qs:
        date=item['bday'].strftime('%y%m%d')
        markup+='<li style="display: inline-block; margin: 5px;"><a href='+'/webGenApp/'+item['firstName']+'>'\
        +item['firstName']+':'+date+'</a></li>'
    markup+='</ul></div>'

    return HttpResponse(markup)

def index(request):
    qs=Person.objects.all().values()
    markup= '<p style="margin-left:50px;">... database initialization ...</p>'
    markup+='<div style="width:1000px;margin-left: 50px;">'
    markup+='<ul >'
    for item in qs:
        date=item['bday'].strftime('%y%m%d')
        markup+='<li style="display: inline-block; margin: 5px;"><a href='+'/webGenApp/'+item['firstName']+'>'\
        +item['firstName']+':'+date+'</a></li>'
    markup+='</ul></div>'

    return HttpResponse(markup)

def test(request,capture):
        qs=Person.objects.filter(firstName=capture).values()

        return render(request,'webGenApp/test.html',context=qs[0])

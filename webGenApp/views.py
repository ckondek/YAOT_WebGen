from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict={"key1":"thisthatandtheother","key2":"me and you"}
    return render(request,'webGenApp/index.html',context=context_dict)

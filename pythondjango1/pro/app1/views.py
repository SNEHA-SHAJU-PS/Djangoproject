from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
     #return HttpResponse("welcome")#or
      #context={'name':'arun','age':23}
      return render(request,'home.html',context={'name':'ayana','age':18})

def index(request):
     #return HttpResponse("Django")
     #context={'course':'python'}
     return render(request, 'index.html',{'course':'python'})

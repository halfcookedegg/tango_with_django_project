from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
   context ={}
   context['name'] = 'testName'
   return render(request,'html test.html',context)
def index1(request):
   context ={}
   context['name'] = 'testName'
   return render(request,'html2.html',context)
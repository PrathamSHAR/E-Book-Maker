from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import books
from django.urls import reverse
from django.http import FileResponse


# Create your views here.
def texteditor(request):
    template =loader.get_template('index.html')
    return HttpResponse(template.render())

def upload(request):
    template =loader.get_template('upload_books.html')
    return HttpResponse(template.render({},request))



def addrecord(request):
    a= request.POST['name'].title()
    b= request.POST['email'].lower()
    c= request.POST['title'].title()
    d= request.POST['genre'].title()
    
    record = books(authorname=a, email=b,title=c,genre=d,cover_page=request.FILES['cover'],file=request.FILES['pdf'])
    record.save()
    return HttpResponseRedirect(reverse('submission'))

def show(request):
    template =loader.get_template('show.html')
    records=books.objects.all().values()
    context={
        'records':records,
        'hit1':5,
        'hit2':30,
        'hit3':20,
        'hit4':40,
        'hit5':60,

    }
    return HttpResponse(template.render(context,request))

def search(request):
    if request.method=='GET':
        query=request.GET.get('q')
        query=query.title()
        submitbutton=request.GET.get('submit')
        records=books.objects.all().filter(
                genre=query
            )
        if records.count()==0:
                records=books.objects.all().filter(
                    title=query
               )
        context={
            'records':records,
            'submitbutton':submitbutton,
            'hit1':5,
            'hit2':30,
            'hit3':20,
            'hit4':40,
            'hit5':60,
        }
        return render(request,'show.html',context)
    
def submission(request):
     template =loader.get_template('submission.html')
     return HttpResponse(template.render({},request))




## Manupulation By Pratham
def rate(request):
     rating=request.GET.get('r')
     print("here is rating",rating)
     

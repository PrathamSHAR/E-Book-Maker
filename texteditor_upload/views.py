from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import books,readrate
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
          
        }
        return render(request,'show.html',context)
    
def submission(request):
     template =loader.get_template('submission.html')
     return HttpResponse(template.render({},request))




## Manupulation By Pratham
def rate(request):
     rating=request.GET.get('r')
     gettitle=request.GET.get('title')
     record1=books.objects.get(title=gettitle)
     totalhits=record1.hitrate
     record1.hitrate=totalhits+1

     # calculating % of rating
     one=record1.onestar
     two=record1.twostar
     three=record1.threestar
     four=record1.fourstar
     five=record1.fivestar
     match int(rating):
          case 1:
               record1.onestar=one+1
               record1.oneper=((one+1)*100)/(totalhits+1)
               record1.fourper=((four)*100)/(totalhits+1)
               record1.twoper=((two)*100)/(totalhits+1)
               record1.threeper=((three)*100)/(totalhits+1)
               record1.fiveper=((five)*100)/(totalhits+1)
               record1.avgrating=((one+1)*1+two*2+three*3+four*4+five*5)/((totalhits+1))
               

          case 2:
               record1.twostar=two+1
               record1.oneper=((one)*100)/(totalhits+1)
               record1.fourper=((four)*100)/(totalhits+1)
               record1.twoper=((two+1)*100)/(totalhits+1)
               record1.threeper=((three)*100)/(totalhits+1)
               record1.fiveper=((five)*100)/(totalhits+1)
               record1.avgrating=(one*1+(two+1)*2+three*3+four*4+five*5)/((totalhits+1))

          case 3:
               record1.threestar=three+1
               record1.oneper=((one)*100)/(totalhits+1)
               record1.fourper=((four)*100)/(totalhits+1)
               record1.twoper=((two)*100)/(totalhits+1)
               record1.threeper=((three+1)*100)/(totalhits+1)
               record1.fiveper=((five)*100)/(totalhits+1)
               record1.avgrating=(one*1+two*2+(three+1)*3+four*4+five*5)/((totalhits+1))

          case 4:
               record1.fourstar=four+1
               record1.oneper=((one)*100)/(totalhits+1)
               record1.fourper=((four+1)*100)/(totalhits+1)
               record1.twoper=((two)*100)/(totalhits+1)
               record1.threeper=((three)*100)/(totalhits+1)
               record1.fiveper=((five)*100)/(totalhits+1)
               record1.avgrating=(one*1+two*2+three*3+(four+1)*4+five*5)/((totalhits+1))

          case 5:
               record1.fivestar=five+1
               record1.oneper=((one)*100)/(totalhits+1)
               record1.fourper=((four)*100)/(totalhits+1)
               record1.twoper=((two)*100)/(totalhits+1)
               record1.threeper=((three)*100)/(totalhits+1)
               record1.fiveper=((five+1)*100)/(totalhits+1)
               record1.avgrating=(one*1+two*2+three*3+four*4+(five+1)*5)/((totalhits+1))
          
               
     record1.save()




     print("here is rating",rating,gettitle)
     return redirect('/bookscollection/')

     

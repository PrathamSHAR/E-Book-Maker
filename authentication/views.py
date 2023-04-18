
import random
from django.shortcuts import  redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from authentication.models import Onetimepassword, Verifytable
from bookgram import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
import datetime
# from django.utils.encoding import force_bytes,force_text
# from . tokens import generate_token
# from django.core.mail import EmailMessage

def home(request):
    fname = request.session.get('fname', None)
    context={
                'fname':fname
            }
    return render(request,'authentication/index.html',context)


def signup(request):
     if request.method=='POST':
       username= request.POST.get('username')
       fname=    request.POST.get('fname')
       lname=    request.POST.get('lname')
       email=    request.POST.get('email')
       pass1=    request.POST.get('pass1')
       pass2=    request.POST.get('pass2')


    #    if User.objects.filter(username=username):
    #        messages.error(request,"Username already exist try some different")
    #        return redirect('home')
       

    #    if User.objects.filter(email=email):
    #        messages.error(request,"email already Registered ,Try login")
    #        return redirect('home')
       
       

       myuser=User.objects.create_user(username,email,pass1)
       myuser.first_name=fname
       myuser.last_name=lname


       myuser.is_active=False
       

       

       
       
       #WELCOME EMAIL
       otp=random.randint(1,9)
       subject="Welcome to bg  - Django Login"
       message= "Hello " + myuser.first_name + " Welcome to Bg Your otp is "+ str(otp)
       from_email=settings.EMAIL_HOST_USER
       to_list=[myuser.email]
       send_mail(subject,message,from_email,to_list,fail_silently=True)

       #Message to Confirm mail
       messages.success(request,' WE have send you an email for conformation please confirm your account Your Account has been successfully created')
       myuser.save()

       myorgotp=Verifytable.objects.create(username=username,otp_num=otp)
       myorgotp.save()


       return render(request,'authentication/otp.html',context={'username':username})



         
     return render(request,"authentication/signup.html")









def signin(request):
    if request.method=='POST':
        username= request.POST.get('username')
        pass1=    request.POST.get('pass1')

        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            request.session['fname'] =fname

            context={
                'fname':fname
            }
            messages.success(request,"You are signed in ,enjoy your journey")
            return render(request,'authentication/index.html',context)

        else:
            messages.error(request,"You Are not registered user First Signup ")
            return redirect('home')
    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"You log out successfully")
    return redirect('home')
    



def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode)
        myuser=User.objects.get(pk=uid)

    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser=None
    
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active=True
        myuser.save()
        login(request,myuser)
        return redirect('home')
    else:
        return render(request,'activation_failed.html')
    


#Email verification using otp
def inputotp(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        otp_x=request.POST.get('otp')
        try:
            myusercred=Verifytable.objects.get(username=username)
            print("The otp_x is",type(otp_x),"and myusercred",type(myusercred.otp_num))
            if(myusercred.otp_num==int(otp_x)):
                myuser=User.objects.get(username=username)
                myuser.is_active=True
                myuser.save()
                print("my user",myuser.is_active)
                return render(request,'authentication/verifyingotp.html')
            else:
                return redirect('home')
        except:
            return redirect('inputotp')
   
        
    return render(request,'authentication/otp.html')

def editor(request):
     return render(request,'editor/index.html')



     
    
    
        



    
    




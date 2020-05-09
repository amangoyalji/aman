from django.shortcuts import render,redirect
from django.http import HttpResponse
import smtplib
import random
num=111111
v=0
def randomnum():
    return random.randrange(100000,999999)

def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")


def contactsubmit(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        try:
            sender_email = "amana6398@gmail.com"
            reciever_email = "gargshivam1712@gmail.com"
            password = "RJ-45Xtreme"
            message=name+" has sent you mail regarding "+message+" having email address - "+email

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message)
            server.sendmail(sender_email, email, message)

            return  render(request,"otpver.html")
        except:
            return HttpResponse("sorry enter the correct details !!!")

    return redirect('contact/')

def about(request):
    return render(request,"about.html")

def login(request):
    return render(request,"login.html")

def submitlogin(request):
    if(request.method=="POST"):
        username=request.POST['username']
        email=request.POST['email']
        try:
            sender_email = "amana6398@gmail.com"
            reciever_email = "jaimala.jha@gmail.com"
            accesser = username
            password = "RJ-45Xtreme"
            message = accesser + "wants to accesee the data having email" + email
            otp=randomnum()
            global num
            num = otp
            message1="the link that you are accessing belongs to jaimala jha\nThe required OTP is:"+str(otp)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message)
            server.sendmail(sender_email, email, message1)

            return  render(request,"otpver.html")
        except:
            return HttpResponse("sorry enter the correct details !!!")

    return render(request,"login.html")

def otpverification(request):
    if(request.method=="POST"):
        otp=request.POST['otp']
        if(int(otp)==num):
            return render(request,"thelink.html")
        else:
            return HttpResponse("sorry you have entered the wrong One Time Password")



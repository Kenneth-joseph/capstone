from django.shortcuts import render,redirect
import pyrebase
from django.contrib import auth

config={
"apiKey": "AIzaSyBBc9k7-hPr8v_a0G9vdcK73CdcWD133vs",
    "authDomain": "capstone-713b5.firebaseapp.com",
    "databaseURL": "https://capstone-713b5.firebaseio.com",
    "projectId": "capstone-713b5",
    "storageBucket": "capstone-713b5.appspot.com",
    "messagingSenderId": "149309002319",
    "appId": "1:149309002319:web:29742468dd3a956fbe503a",
    "measurementId": "G-1YSEVXCJ78",
    
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
 

# Create your views here.
def signin(request):
    
    return render(request, 'signin.html')

def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')

    try:

        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message={'invalid credentials'}
        return render(request,'signin.html',{'message':message})

    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)

    return render(request,'welcome.html',{'email':email})

def logout(request):
    auth.logout(request)
    return render(request,'signin.html')

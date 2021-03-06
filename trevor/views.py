from django.shortcuts import render,redirect
import pyrebase
from django.contrib import auth

import time
from datetime import datetime,timezone
import pytz

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
database=firebase.database()#initialising the database
 

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

def signUp(request):

    return render(request,'signUp.html')

def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')    
    passw=request.POST.get('pass')

    try:
        user = authe.create_user_with_email_and_password(email, passw)#creating the account

    except:
        message='unable to create account try again'
        return render(request,'signin.html',{'message':message})
        uid=user['localId']#getting the local id which is unique for everyone
        
    data={'name':name,"status":"1"}#status for enabling this account data for getting the name vaule
    database.child('users').child(uid).child('details').set(data)# create constructor called child which enables many users to be entered and it collects the uid and details

    return render(request,'signin.html')

def create(request):

    return render(request,'create.html')

def postcreate(request):
    # import time
    # from datetime import datetime,timezone
    # import pytz
    tz=pytz.timezone('Africa/Nairobi')
    time_now=datetime.now(timezone.utc).astimezone(tz)#converts utc time right now to the timezone you are in
    millis=int(time.mktime(time_now.timetuple()))#converts time in miliseconds
    print('mili'+str(millis))
    work=request.POST.get('work')
    progress=request.POST.get('progress')


    idtoken=request.session['uid']
    a=authe.get_account_info(idtoken)
    a=a['users']
    a=a[0]
    a=a['localId']
    print('info'+str(a)),
    data = {
        'work':work,
        'progress':progress
            }
    database.child('users').child(a).child('reports').child(millis).set(data)
    name = database.child('users').child(a).child('details').child('name').get().val()

    return render (request,'welcome.html',{'email':name})
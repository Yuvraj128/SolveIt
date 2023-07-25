from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Messages, Profile
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from datetime import datetime

# Create your views here.
def dummy_home(request,key):
    print("key is ....................", key)
    
    if key=='api_key':
        messages = Messages.objects.all()
        # print(messages.values())
        return JsonResponse({'messages':list(messages.values())})

    return HttpResponse("Not allowed to access this api key.")


def home(request):
    # chats = Messages.objects.all()
    # username = request.user.username
    return render(request,'home.html')

@login_required(login_url='/')
def chats_show(request):
    user = request.user.username
    user_id = Profile.objects.get(username=user).id
    msg = Messages.objects.get(id=72)
    print(user_id,"from chats_show mein hai abhi hum yaha se ye ja raha",msg.timing.minute)
    return render(request,'index.html',{'id':user_id})

def login_user(request):
    print("current time is this ",datetime.now())
    if request.method=="POST":
        username = request.POST['username']
        password = '1234'
        user = authenticate(username=username,password=password)
        # print(user,username)
        if user:
            # print("inside if ")
            login(request,user)
            return redirect('chats')
        # return redirect('chat/messages')
        else:
            # messages.success(request,'The New User '+request.POST['username']+ ' is saved Successfully...!')
            # return render(request, 'login.html')
        # else:
            messages.warning(request, 'you are not registered '+username)
            return render(request, 'home.html')

    return render(request,'home.html')

def signup_user(request):
    username = request.POST['username']
    password = request.POST['password']
    User.objects.create_user(username=username,password=password).save()
    messages.success(request,'The New User '+ username + ' is saved Successfully...!')
    return redirect('chats')


@login_required(login_url='/')
def chat(request): 
    chats = Messages.objects.all()
    username = request.user.username
    id = Profile.objects.get(username=username)
    print("iddddddddddddddddddddddddddddddddddd", id)
    return JsonResponse({'chats':list(chats.values())}) 
    # return render(request,'index.html',{'chats':list(chats.values())})

    # chats = Messages.objects.all()
    # username = request.user.username
    # return render(request,'index.html',{'username':username,'chats':chats}) 


@login_required(login_url='/')
def sent_msg(request):
    message  = request.POST.get('message_user','dummy msggggg ha ha')
    # print(message)
    user = request.user.username
    print("we are in the sent msg function see here see here ",user,message)
    profile = Profile.objects.get(username=user)
    print("we are here in sent msg and the profile is ",profile)
    Messages.objects.create(user=profile,message=message).save()
    return HttpResponse('Message sent successfully')



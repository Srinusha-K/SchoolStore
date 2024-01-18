from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def demo(request):
    return render(request,'base.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/studentapp/add')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('/login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword= request.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/register')
            else:
                user =User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('/login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('/register')

    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
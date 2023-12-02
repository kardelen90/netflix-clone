from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return redirect('profilPage')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = CustomUser.objects.get(email = email).username
            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)

                nxt = request.GET.get('next',None)
                if nxt is not None:
                    return redirect(nxt)
                else:
                    return redirect('profilPage') 
            else:
                return render(request,'login.html',{
                    'form':form
                })
        else:
            return render(request,'login.html',{
                'form':form
            })
    form = LoginForm()
    return render(request,'login.html',{
        'form':form
    })


def register_request(request):
    if request.user.is_authenticated:
        return redirect('profilPage')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request,username = username, password = password)
            login(request,user)
            return redirect('profilPage')
        else:
            return render(request,'register.html',{
                'form':form
            })
    form = RegisterForm()
    return render(request,'register.html',{
        'form':form
    })

def logout_request(request):
    logout(request)
    return redirect('indexPage')

@login_required(login_url='/login/')
def profil(request):
    if request.method == 'POST':
        id = request.POST['gizle']
        silinecek = Profile.objects.get(id = id)
        silinecek.delete()
      
    return render(request,'profil.html')

@login_required(login_url='/login/')
def profil_manage(request,slug):
    if request.method == 'POST':
        form = CreateProfile(request.POST,request.FILES)
        if form.is_valid():
            if request.user.profil_counter() < 5:
                profil = form.save(commit=False)
                profil.owner = request.user
                profil.save()
                return redirect('profilPage')
            else:
                messages.error(request,'Acabılecegınız profıl sayısı en fazla 5 dir.')
                return redirect('profilPage')
        else:
           return render(request,'profil-manage.html',{
                'form':form
            })  
    if request.user.profil_counter() == 5:
        messages.error(request,'Acabılecegınız profıl sayısı en fazla 5 dir.')
        return redirect('profilPage')
    form = CreateProfile()
    return render(request,'profil-manage.html',{
        'form':form
    })
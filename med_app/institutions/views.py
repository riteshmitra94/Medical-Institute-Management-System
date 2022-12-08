from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import *
from .forms import InstituteForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

@login_required(login_url='login')
def Home(request):
    #return HttpResponse('Welcome Page')
    return render(request, 'institutions/landingPage.html')

@login_required(login_url='login')
def addInstitution(request):

    form = InstituteForm()

    if request.method == 'POST':
        #print('printing POST: ',request.POST)
        form = InstituteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/institutions')

    context = {'form' : form}

    return render(request, 'institutions/addInstitute.html', context)

@login_required(login_url='login')
def updateInstituteInfo(request, inst_Id):

    institute = Institute.objects.get(id=inst_Id)
    form = InstituteForm(instance=institute)
    if request.method == 'POST':
        #print('printing POST: ',request.POST)
        form = InstituteForm(request.POST, instance=institute)
        if form.is_valid():
            form.save()
            return redirect('/institutions')
    
    context = {'form' : form}

    return render(request, 'institutions/addInstitute.html', context)

@login_required(login_url='login')
def showInstitutions(request):
    institutions = Institute.objects.all()

    total_institutions  = institutions.count()
    active_institutions = institutions.filter(status='Active').count()
    
    context = {'institutions' : institutions, 'total_institutions' : total_institutions, 'active_institutions' : active_institutions}

    return render(request, 'institutions/institutions.html', context)

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            #print('Before Logged In User: ',request.POST.get('username'), request.POST.get('password'))
            user = authenticate(request, username=username, password=password)
            #print('Logged In User: ',user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                #print(user)
                messages.info(request, 'Username or password is incorrect, please try again')
        
    context={}
    return render(request, 'institutions/login.html', context)

def Register(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'User Account has been created for '+ user)

                return redirect('login')

    context = {'form': form}

    return render(request, 'institutions/register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def showUserInfo(request):
    return render(request, 'institutions/userInfo.html')

@login_required(login_url='login')
def showInstituteInfo(request, inst_Id):
    instituteDetails  = Institute.objects.get(id=inst_Id)

    context = {'instituteDetails' : instituteDetails}

    return render(request, 'institutions/instituteInfo.html', context)
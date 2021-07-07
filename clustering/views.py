from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import CustomerForm, DataForm, CreateUserForm
from .decorators import unauthenticated_user

import pickle

# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for '+username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)    
            return redirect('base') 
        else:
            messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def base(request):
    return render(request, 'base.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'main.html')

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    context = {'customer': customer}
    return render(request, 'user.html', context)

@login_required(login_url='login')
def data(request):
    data = Data.objects.all()
    print(data)
    context = {'data':data}
    return render(request, 'data.html', context)

@login_required(login_url='login')
def predict(request):
    return render(request, 'predict.html')

@login_required(login_url='login')
def result(request):
    kmeans_model = pickle.load(open('./models/kmeans.pkl', 'rb'))
    kelurusan = request.GET['kelurusan']
    elevasi = request.GET['elevasi']
    geologi = request.GET['geologi']
    jalan = request.GET['jalan']
    kel = request.GET['kel']
    lahan = request.GET['lahan']
    sungai = request.GET['sungai']
    tanah = request.GET['tanah']
    hujan = request.GET['hujan']
    aspek = request.GET['aspek']
    value = [[kelurusan, elevasi, geologi, jalan, kel, lahan, sungai, tanah, hujan, aspek]]

    pred = kmeans_model.predict(value)

    context = {'pred': pred}
    return render(request, 'predict.html', context)

@login_required(login_url='login')
def userPage(request):
    user  = request.user.all()
    context = {'user':user}
    return render(request, 'user.html', context)

@login_required(login_url='login')
def createData(request):
    form = DataForm()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'order_form.html', context)

@login_required(login_url='login')
def updateData(request, pk):
    data = Data.objects.get(id=pk)
    form = DataForm(instance=data)
    if request.method == 'POST':
        form = DataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'data':data, 'form':form}
    return render(request, 'order_form.html', context)

@login_required(login_url='login')
def deleteData(request, pk):
    data = Data.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('/')

    context = {'item':data}
    return render(request, 'delete.html', context)

@login_required(login_url='login')
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'account_settings.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from blogs.models import category, blog
from assignments.models import About
from blog_main.forms import RegisterationForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login 
from django.contrib import auth






def home(request):
    # categories= category.objects.all()
    featured_blogs = blog.objects.filter(is_featured=True)
    unfeatured_blogs = blog.objects.filter(is_featured=False)
    
    try:
        about = About.objects.get()
    except About.DoesNotExist:
        about = None
    context= {
        # 'categories': categories,    #brought from context processor
        'featured_blogs': featured_blogs,
        'unfeatured_blogs': unfeatured_blogs,
        'about': about,         
        
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register') 
        else:
            print(form.errors)      
    else:
        form = RegisterationForm()
    context = {
            'form': form,
        }           
    return render(request, 'register.html', context) 


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
               auth.login(request, user) 
            return redirect('dashbord') 
        else:
            print(form.errors)
    form = AuthenticationForm()
    context = {
        'form': form,
    }       

    return render(request, 'login.html', context)    


def logout(request):
    auth.logout(request)
    return redirect('home')     


    

   


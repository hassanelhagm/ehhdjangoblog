from django.shortcuts import render, redirect
from blogs.models import category
from blogs.models import blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
from django.shortcuts import get_object_or_404
from .forms import blogpostForm
from django.utils.text import slugify
from django.contrib.auth.models import User
from .forms import AddUserForm
from .forms import EditUserForm


# Create your views here.
@login_required(login_url='login')
def dashbord(request):
    category_count=category.objects.all().count()
    post_count=blog.objects.all().count()
    context={
        'category_count':category_count,
        'post_count':post_count
    }
    return render(request, 'dashbord/dashbord.html',context)

def categories(request):
    return render(request, 'dashbord/categories.html')  

def add_category(request):
    form=CategoryForm()
    context={
        'form':form
    }           
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()   
            return render(request, 'dashbord/categories.html')
    return render(request, 'dashbord/add_category.html' ,context)   



def edit_category(request, pk):
    category_instance = get_object_or_404(category, id=pk)
    form = CategoryForm(instance=category_instance)
    if request.method == 'POST':
       form = CategoryForm(request.POST, instance=category_instance)
       if form.is_valid():
            form.save()
            return render(request, 'dashbord/categories.html')
    context = {
        'form': form,
        'category_instance': category_instance
    }
    
    return render(request, 'dashbord/edit_category.html', context)    # Edit existing category           
      



def delete_category(request, pk):   
    category_instance = get_object_or_404(category, id=pk)
    category_instance.delete()
    return render(request, 'dashbord/categories.html')
    context = {
        'category_instance': category_instance
    }
    return render(request, 'dashbord/categories.html', context)  # Delete existing category  


def posts(request):
    posts = blog.objects.all()
    context = {
        'posts': posts
    }           
    return render(request, 'dashbord/posts.html', context)  

def add_post(request):
    if request.method=='POST':
        form=blogpostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the current user
            post.save()
            title = form.cleaned_data['title']
            post.slug= slugify(title) + '-' + str(post.id)
            post.save()
            
            return redirect('posts')
        else:
            print("form is not valid")   
            print(form.errors)   
    form=blogpostForm()
    context={   
        'form': form
    }    
    return render(request, 'dashbord/add_post.html', context)  # Add new post 

def edit_post(request, pk):
    post_instance = get_object_or_404(blog, id=pk)
    form = blogpostForm(instance=post_instance)
    if request.method == 'POST':
       form = blogpostForm(request.POST, request.FILES, instance=post_instance)
       if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug= slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    context = {
        'form': form,
        'post_instance': post_instance
    }
    
    return render(request, 'dashbord/edit_post.html', context)  # Edit existing post  

def delete_post(request, pk):
    post_instance = get_object_or_404(blog, id=pk)
    post_instance.delete()
    return redirect('posts')  


def users(request):
    users=User.objects.all()
    context={           
        'users': users
    }           
            
    return render(request, 'dashbord/users.html', context)  # User management page    

def add_user(request):
    if request.method=='POST':
        form=AddUserForm(request.POST)
        if form.is_valid():
            form.save()   
            return redirect('users')
        else:
            print("form is not valid")   
            print(form.errors)
    form=AddUserForm()
    context={               
        'form': form
    }
    return render(request, 'dashbord/add_user.html', context)  # Add new user

def edit_user(request, pk):
    user_instance = get_object_or_404(User, id=pk)
    form = EditUserForm(instance=user_instance)
    if request.method == 'POST':
       form = EditUserForm(request.POST, instance=user_instance)
       if form.is_valid():
            form.save()
            return redirect('users')
    context = {
        'form': form,
        'user_instance': user_instance
    }
    
    return render(request, 'dashbord/edit_user.html', context)  # Edit existing user   

def delete_user(request, pk):
    user_instance = get_object_or_404(User, id=pk)
    user_instance.delete()
    return redirect('users')  # Delete existing user    




from django.shortcuts import render, redirect
from .models import blog, category
from django.db.models import Q
from .models import comment
from django.http import HttpResponseRedirect

# Create your views here.
def posts_by_categoryId(request, category_id):
    # Logic to retrieve posts by category_id
    posts = blog.objects.filter(status='published', category=category_id)
    category_name = category.objects.get(id=category_id)
    
    context = {
        'category_id': category_id,
        'posts': posts,
        'category_name': category_name
         }
    
    return render(request, 'posts_by_category.html', context )


def blogs(request, slug):
    blog_post = blog.objects.get(slug=slug, status='published')
    if request.method == 'POST':
       commentadd = comment() 
       commentadd.user = request.user
       commentadd.blog = blog_post
       commentadd.comment = request.POST.get('comment') 
       commentadd.save()
       return HttpResponseRedirect(request.path_info)

       
    comments= comment.objects.filter(blog=blog_post)
   
             
    context = {
            'blog_post': blog_post,
            'comments': comments,
        }
    return render(request, 'blog_detail.html', context)

def search(request):
    query = request.GET.get('keyword', '')
    results = blog.objects.filter(Q(title__icontains=query) | Q(short_description__icontains=query)   | Q(blog_body__icontains=query)  , status='published')
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'search.html', context)      


        
   

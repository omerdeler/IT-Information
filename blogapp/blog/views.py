from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog,Category




def index(request):
    
    context = {
        "blogs":Blog.objects.filter(is_home=True, is_active=True),    # Blog.objects.all() blogs bilgisini data icerisindn gelen blogtan aldık
        "categories": Category.objects.all()
    
    }
    return render(request, "blog/index.html", context)



def blogs(request):
    context = {
        "blogs":Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()  
    }
    return render(request, "blog/blogs.html", context)



def blogs_details(request, slug):
    blog = Blog.objects.get(slug=slug)


    return render(request, "blog/blog_details.html ", { 
        "blog" : blog 
    })


def blogs_by_category(request, slug):
    context = {
        "blogs":Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)
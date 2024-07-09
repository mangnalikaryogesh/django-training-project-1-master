from django.shortcuts import render, redirect, get_object_or_404
from . models import Category,Tag,Post,Comment
from django.db import models
from django.http import Http404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db.models import Count

#define constants
number_of_blogposts = 10

def blog(request):
    blogposts = Post.objects.filter(published = True)
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))   #Note, related name is the lowercase of the name of the model
    blog_tags = Tag.objects.all()
    
    #recent blogs
    recent_posts = Post.objects.order_by('-created_at')[:5]
    # context = {"blogposts": blogposts,'blog_categories':blog_categories,'blog_tags':blog_tags,'recent_posts':recent_posts}
     # Pagination
    paginator = Paginator(blogposts, number_of_blogposts)  # Change 10 to the number of posts per page you want
    page = request.GET.get('page')
    try:
        blogposts = paginator.page(page)
    except PageNotAnInteger:
        blogposts = paginator.page(1)
    except EmptyPage:
        blogposts = paginator.page(paginator.num_pages)
    
    context = {
        "blogposts": blogposts,
        'blog_categories': blog_categories,
        'blog_tags': blog_tags,
        'recent_posts': recent_posts
    }
    
    
    return render(request,'blog.html',context)



def post_list_by_category(request, category_slug):
    try:
        #fetch and count blog categories
        blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
        
        #fetch tags
        blog_tags = Tag.objects.all()
        
        #recent blogs
        recent_posts = Post.objects.order_by('-created_at')[:5]
        
        # Retrieve the category object based on the slug
        selected_blog_categories = Category.objects.get(url=category_slug)
        
        
        # Retrieve all posts belonging to the specified category
        blogposts = Post.objects.filter(categories=selected_blog_categories, published=True)
        
        context = {"blogposts": blogposts,'blog_categories':blog_categories,'blog_tags':blog_tags,'recent_posts':recent_posts}
       
        return render(request, 'blog.html', context)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")



def post_detail(request, url):
    post = get_object_or_404(Post, url=url)
    approved_blogs = Post.objects.filter(published=True)
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    # recent blogs
    recent_posts = Post.objects.order_by('-created_at')[:5] 
    comments = post.comments.filter(approved=True)  # Filter comments for the specific post
    
    #TAGS
    blog_tags = Tag.objects.all()
    
    current_blog_tag = post.tags.all()
    # print(current_blog_tag)
    
    

    context = {
        'post': post,
        'blogs': approved_blogs,
        'blog_categories': blog_categories,
        'recent_posts': recent_posts,
        'comments': comments,
        'blog_tags':blog_tags,
        'current_blog_tag':current_blog_tag
    }
    return render(request, 'single.html', context)

# @login_required(login_url='login')
def postcomment(request):
    if request.method == "POST":
        url = request.POST['url']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        post = get_object_or_404(Post, url=url)
        comment = Comment.objects.create(post=post,author=name, email=email, content=message)
        response_data = {
            "saved": True
        }
        return JsonResponse(response_data)
        

def blog_search(request):
    query = request.GET.get('q')
    if query:
        # Perform search using filter or other methods based on your requirements
        blogposts = Post.objects.filter(title__icontains=query, published=True)
    else:
        blogposts = None
    
    # blogposts = Post.objects.filter(published = True)
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))   #Note, related name is the lowercase of the name of the model
    blog_tags = Tag.objects.all()
    
    #recent blogs
    recent_posts = Post.objects.order_by('-created_at')[:5]
    context = {
        "blogposts": blogposts ,
        'blog_categories': blog_categories,
        'blog_tags': blog_tags,
        'recent_posts': recent_posts,
        'query': query
    }
    
    return render(request, 'search_results.html', context)


def tag_filter(request, tag_slug):
    tag = Tag.objects.get(name=tag_slug)
    blogposts = Post.objects.filter(tags=tag, published=True)
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))   #Note, related name is the lowercase of the name of the model
    blog_tags = Tag.objects.all()
    
    #recent blogs
    recent_posts = Post.objects.order_by('-created_at')[:5]
    # context = {"blogposts": blogposts,'blog_categories':blog_categories,'blog_tags':blog_tags,'recent_posts':recent_posts}
     # Pagination
    paginator = Paginator(blogposts, number_of_blogposts)  # Change 10 to the number of posts per page you want
    page = request.GET.get('page')
    try:
        blogposts = paginator.page(page)
    except PageNotAnInteger:
        blogposts = paginator.page(1)
    except EmptyPage:
        blogposts = paginator.page(paginator.num_pages)
    
    
    
    context = {
        "blogposts": blogposts ,
        'blog_categories': blog_categories,
        'blog_tags': blog_tags,
        'recent_posts': recent_posts,
        
    }
    return render(request, 'blog.html', context)




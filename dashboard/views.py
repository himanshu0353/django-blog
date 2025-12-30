from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, PostForm
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count() 
    blogs_count = Blog.objects.all().count()
    context={
        "category_count": category_count,
        "blogs_count":blogs_count,
    }
    return render(request, 'dashboard/dashboard.html',context)

def Categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:categories')
    form = CategoryForm()
    context ={
        'form':form,
    }
    return render(request, 'dashboard/add_category.html',context )

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category,
    }
    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('dashboard:categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'dashboard/posts.html', context)

def add_posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # Let AutoSlugField on the model set the slug on save
            post.save()
            return redirect('dashboard:posts')
    form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'dashboard/add_post.html', context)

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard:posts')
   
    form = PostForm(instance=post)
    context = {
        'post':post,
        'form':form,
    }
    return render(request, 'dashboard/edit_posts.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return render(request, 'dashboard:posts')
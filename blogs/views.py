# coding:utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
import time

# Create your views here.
from django.urls import reverse

from blogs.forms import BlogEntity
from blogs.models import Blog


def home(request):
    return render(request, 'blogs/home.html')


def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog.html', context)


# 进入添加Blog页面
def addEntity(request):
    from blogs.forms import BlogEntity
    form = BlogEntity
    return render(request, reverse('blogs:'))


# 添加blog
def newEntity(request):
    if request.method == 'POST':
        form = BlogEntity(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            title = str(title)
            content = str(content)
            createTime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            updateTime = createTime
            from blogs.models import Blog
            Blog.objects.create(title=title, content=content, createTime=createTime, updateTime=updateTime, )
            return HttpResponseRedirect(reverse('blogs:manageBlog'))
    else:
        form = BlogEntity()
        return render(request, 'blogs/newEntity.html', {'form': form})


# edit
def editEntity(request, blog_id):
    from .models import Blog
    if request.method == 'POST':
        form = BlogEntity(request.POST)
        if form.is_valid():
            blog = Blog.objects.get(id=blog_id)
            blog.title = form.cleaned_data.get('title')
            blog.content = form.cleaned_data.get('content')
            blog.updateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            # title = str(title)
            # content = str(content)
            blog.save()
            return HttpResponseRedirect(reverse('blogs:blog', kwargs={'blog_id': blog_id}))
    else:

        blog = Blog.objects.get(id=blog_id)
        form = BlogEntity(initial={'title': blog.title, 'content': blog.content})
        context = {'form': form, 'blog': blog}
        return render(request, 'blogs/editEntity.html', context)


def deleteBlog(request,blog_id):
    from blogs.models import Blog
    Blog.objects.get(id=blog_id).delete()
    return HttpResponseRedirect(reverse('blogs:manageBlog'))


def selectBlog(request, blog_id):
    pass


def manageBlog(request):
    from blogs.models import Blog
    blogs = Blog.objects.all()
    return render(request, 'blogs/manage_blog.html', {'blogs': blogs})

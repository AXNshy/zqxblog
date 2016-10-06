#coding:utf-8
from django.shortcuts import render
import time

# Create your views here.
from blogs.forms import BlogEntity


def home(request):
    return render(request, 'blogs/home.html')

# 进入添加Blog页面
def addEntity(request):
    from blogs.forms import BlogEntity
    form = BlogEntity
    return render(request, 'blogs/newEntity.html', {'form': form})


# 添加blog
def newEntity(request):
    if request.method=='POST':
        form = BlogEntity(request.POST)
        if form.is_valid():
            title = request.GET['title']
            content = request.GET['content']
            title = str(title)
            content = str(content)
            createTime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            updateTime = createTime
            from blogs.models import Blog
            Blog.objects.create(title=title, content=content, createTime=createTime, updateTime=updateTime,)
            from django.http import HttpResponse
            return HttpResponse('ok')

def deleteBlog(request):
    title = request.GET['title']
    from blogs.models import Blog
    Blog.delete(title='django is a very light web developing frame')

def selectBlog(request):
    from blogs.models import Blog
    pass

def manageBlog(request):
    from blogs.models import Blog
    blogs = Blog.objects.all()
    return render(request, 'blogs/manage_blog.html', {'blogs': blogs})

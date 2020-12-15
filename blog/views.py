from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.
def blogHome(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request,'blog/blogHome.html', context)

def blogPost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    post.views= post.views +1
    post.save()
    return render(request,'blog/blogPost.html', context)

def home(request):
    return render(request,'home/index.html')
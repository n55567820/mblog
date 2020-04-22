from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from .models import Post


# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,'index.html',locals())

def showpost(request,slug):
    try:
        post = Post.objects.get(slug = slug)
        if post!= None:
            return render(request,'post.html',locals())
    except:
        return redirect('/')





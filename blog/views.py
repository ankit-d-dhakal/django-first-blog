from django.shortcuts import render,redirect
from blog.models import Post

def index(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', ctx)


def single(request, id):
    post = Post.objects.get(id=id)
    ctx = {
        'post': post,
    }
    return render(request, "blog/blog-single.html", ctx)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        content = request.POST.get('content')
        Post.objects.create(title=title, summary=summary, content=content)
        # Post.objects.create(summary=summary)
        # Post.objects.create(content=content)
        return redirect('index')
    return render(request, 'blog/blog-create.html') 

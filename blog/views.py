from django.shortcuts import redirect, render

from blog.models import Post


def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-views')
    ctx = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', ctx)


def single(request, id):
    post = Post.objects.get(id=id)
    post.views += 1
    post.save() 
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

def edit(request):
    pass  

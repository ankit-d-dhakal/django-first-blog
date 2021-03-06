from django.shortcuts import redirect, render

from blog.models import Post


def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-id')
    ctx = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', ctx)


def single(request, slug):
    post = Post.objects.get(slug=slug)
    post.views += 1
    post.save()
    print(post.category.title) 
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
        return redirect('index')
    return render(request, 'blog/blog-create.html')

def edit(request):
    pass  

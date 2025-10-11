from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.

def starting_page(request):
    all_posts = Post.objects.all().order_by('-date')[:3]
    return render(request,'blog/index.html',{
        'posts':all_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request,'blog/all-posts.html',{'posts':all_posts})

def single_post(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'blog/post-detail.html',{'post':post, 'post_tages':post.tag.all()})


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView , DeleteView
from .models import Post
# Create your views here.

#class of starting page
class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def starting_page(request):
#     all_posts = Post.objects.all().order_by('-date')[:3]
#     return render(request,'blog/index.html',{
#         'posts':all_posts
#     })

#class of all post
class AllPostView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-date']


# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#     return render(request,'blog/all-posts.html',{'posts':all_posts})

class SinglePostView(DeleteView):
    template_name = 'blog/post-detail.html'
    model = Post
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['post_tages'] = self.object.tag.all()
        return context
    

# def single_post(request, slug):
#     post = get_object_or_404(Post, slug = slug)
#     return render(request, 'blog/post-detail.html',{'post':post, 'post_tages':post.tag.all()})


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)
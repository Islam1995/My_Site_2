from django.shortcuts import render, get_object_or_404 , redirect
from django.views.generic import ListView , DeleteView
from django.views import View
from .models import Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
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

class SinglePostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later
        
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
       
        context = {
            'post':post,
            "post_tags": post.tag.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id"),
            "save_for_later":self.is_stored_post(request, post.id)
        }
        return render(request, 'blog/post-detail.html',context)
    
    def post(self,request,slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail-page',slug=slug)
        #HttpResponseRedirect(reverse("post-detail-page"), args=[slug])
        context = {
            'post':post,
            "post_tags": post.tag.all(),
            "comment_form":CommentForm,
            "comments":post.comments.all().order_by("-id"),
            "save_for_later":self.is_stored_post(request, post.id)
        }

        return render(request, 'blog/post-detail.html',context)
    

class ReadLater(View):
    def get(self,request):
        stored_posts = request.session.get("stored_posts")

        context ={}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in =stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        return render(request, 'blog/stored-posts.html', context)
    
    def post(self,request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST['post_id'])
        
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session['stored_posts'] = stored_posts 
        return redirect("/")


    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context['post_tages'] = self.object.tag.all()
    #     context['comment_form'] = CommentForm()
    #     return context

    
    

# def single_post(request, slug):
#     post = get_object_or_404(Post, slug = slug)
#     return render(request, 'blog/post-detail.html',{'post':post, 'post_tages':post.tag.all()})


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)
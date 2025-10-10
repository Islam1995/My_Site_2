from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request,'blog/index.html')

def posts(request):
    return render(request,'blog/all-posts.html')

def single_post(request, slug):
    return render(request, 'blog/post-detail.html')


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)
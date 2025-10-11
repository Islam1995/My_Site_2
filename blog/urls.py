from django.urls import path
# from django.conf.urls import handler404
from . import views
urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting-page'),
    #path('',views.starting_page, name='starting-page'),
    path('posts',views.AllPostView.as_view(), name='posts-page'),
    #path('posts',views.posts, name='posts-page'),
    path('posts/<slug:slug>',views.SinglePostView.as_view(),name='post-detail-page'),
    # path('posts/<slug:slug>',views.single_post,name='post-detail-page'),
]
# handler404='blog.views.custom_404'
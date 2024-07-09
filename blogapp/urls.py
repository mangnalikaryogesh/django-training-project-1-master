from django.urls import path
from . import views

urlpatterns = [ 
    path('blog/',views.blog,name='blog'),
    path('post/<slug:url>', views.post_detail, name='postdetail'),
    path('postcomment', views.postcomment, name='postcomment'),
    path('category/<slug:category_slug>/', views.post_list_by_category, name='post_list_by_category'),
    path('search/', views.blog_search, name='blog_search'),
    path('tag/<slug:tag_slug>/', views.tag_filter, name='tag_filter'),
   
]
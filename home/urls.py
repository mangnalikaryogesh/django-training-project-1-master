from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('courses/',views.courses,name='courses'),
    path('teachers/',views.teachers,name='teachers'),
    path('subjects/',views.get_subjects,name='get_subjects'),
    # path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("logout/",views.logout,name="logout"),
]
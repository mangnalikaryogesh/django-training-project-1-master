from . models import courseOffered,subjects
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import models
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

# Create your views here.

def index(request):
    all_courses = courseOffered.objects.all()
    context = {
        'all_courses':all_courses
    }
    return render(request,'index.html',context)


def get_subjects(request):
    all_subjects = subjects.objects.all().values()
    all_subjects_list = list(all_subjects)
    return JsonResponse({'data': all_subjects_list})
    
    

def about(request):
    return render(request,'about.html')

def courses(request):
    all_courses = courseOffered.objects.all()
    # all_subjects = subjects.objects.all()
    all_subjects = subjects.objects.annotate(course_count=models.Count('courseoffered'))
    
    context = {"allcourses":all_courses,"allsubjects":all_subjects}
    return render(request,'course.html',context)


def teachers(request):
    return render(request,'teacher.html')



def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message_instance = request.POST["message"]
        message = "Name is : {}\nEmail {}\n{}".format(name,email,message_instance)
        try:
            send_mail(
                    subject,
                    message,
                    email, #sender
                    ['inmotion@dtechnologys.com',], #receipient
                    fail_silently=False,
                )
            # return "Email sent successfully"
            # return "Validation Error: {}".format(e)
        except Exception as e:
            return "An error occurred: {}".format(e)
        
    return render(request,'contact.html')




def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            User = auth.authenticate(username=username,password=password)

            if User is not None:
                auth.login(request,User)
                if request.GET.get('next',None):
                    return HttpResponseRedirect(request.GET['next'])
                return redirect('/')
            else:
                messages.info(request,'Invalid credentials')
                return render(request,'login.html')
            
        else:
            return render(request,'login.html')
    else:
        return redirect("/")


    # return render(request,'login.html')
    



def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Taken!")
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is Taken!")
                return render(request,'register.html')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
                user.save()
                messages.info(request,"New user created!")
                return redirect('login')
        else:
            messages.info(request,"Password not matching!")
            return render(request,'register.html')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

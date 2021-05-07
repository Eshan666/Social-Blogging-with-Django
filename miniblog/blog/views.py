from django.shortcuts import render,redirect
from blog.models import BlogPost

from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.

def home(request):

   
    return render(request,'blog/home.html')

def loginPage(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user =  authenticate(request, username=username, password=password)
            

            if user is not None:
                login(request,user)
                messages.success(request,"Login Successful")
                return redirect('dashBoardPage')
            else:
                messages.info(request,"username or password is incorrect")
    return render(request,'blog/login.html')

def logoutPage(request):
    logout(request)
    messages.success(request, 'Your are now logged out!')
    return redirect('loginPage')


def signupPage(request):
    form =  CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created for '+ user)
            user = form.cleaned_data.get('username')
            return redirect('loginPage')

    context = {'form' : form }
    return render(request,'blog/signup.html',context)
        

def aboutPage(request):
    return render(request,'blog/about.html')

def contactPage(request):
    return render(request,'blog/contact.html')

def dashBoardPage(request):
    all_posts = BlogPost.objects.all()
    context = {"all_posts": all_posts}

    return render(request,'blog/dashboard.html',context)
    
def myProfilePage(request):
    
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        post = BlogPost(author = request.user,title=title,description=description)
        post.save()
        messages.success(request, 'Your post is published successfully')


    my_posts = BlogPost.objects.filter(author = request.user)
    context = {"my_posts":my_posts}
    

    return render(request,'blog/myProfile.html',context)

def updatePost(request,pk):
    post = BlogPost.objects.get(id=pk)
    print(post)
    context = {"post":post}

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        post.title = title
        post.description = description
        post.save() 
        return redirect('myProfilePage')

    return render(request,'blog/updatePost.html',context)

def deletePost(request,pk):
    post = BlogPost.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('myProfilePage')

    return render(request, 'blog/deletePost.html')

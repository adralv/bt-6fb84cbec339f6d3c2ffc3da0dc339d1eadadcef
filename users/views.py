from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .models import UserProfile
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successful login!")
            return redirect('index')
        else:
            messages.error(request, 'Invalid login! Try agian.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

    # else:
    #     messages.error(request, "You must login first.")
    #     return redirect('login')
    # return render(request, 'accounts/logout.html')

def register(request):
    if request.method == "POST":
        # get data from form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        graduation_year = request.POST.get('graduation_year')
        profile_picture = request.FILES.get('profile_image')  # handle file upload

        # password match check
        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # username and email uniqueness check
        if User.objects.filter(username=username).exists():
            messages.error(request, "That username is taken!")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "That email is being used!")
            return redirect('register')

        # create the user
        new_user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        new_user.save()

        # create user profile with image and graduation year
        user_profile = UserProfile.objects.create(
            user=new_user,
            graduation_year=graduation_year,
            profile_picture=profile_picture
        )
        user_profile.save()

        messages.success(request, "User is created! You may log in.")
        return redirect('login')
    
    else:
        return render(request, 'accounts/register.html')
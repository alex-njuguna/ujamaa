from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Profile

def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email not available')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Invalid username')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, 
                    password=password1)
                user.save()

                # log user in and direct to settings page

                # create a profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'Passwords not matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

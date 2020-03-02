from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import User, UserProfile
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm


def user_registration(request):
    user_form = RegistrationForm()

    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Successful registration')

            return redirect(reverse('users:login'))
        else:
            print(user_form.errors)

    messages.warning(request, "Your data hasn't been saved. Please try again")

    return render(request, 'users/registration.html', {
        "user_form": user_form,
    })


def user_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            user = authenticate(request, username=email, password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                messages.success(request, "You're logged in.")

                return redirect(
                    reverse('users:profile', kwargs={'uuid': user.userprofile.unique_id})
                )

            else:
                messages.error(request, "Invalid username or password")

        else:
            messages.error(request, "Invalid input")

    return render(request, 'users/login.html', {
        'form': form,
        'title': 'Login page'
    })

@login_required
def user_profile(request, uuid):
    other_users = UserProfile.get_others()

    return render(request, 'users/profile.html')

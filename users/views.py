from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.db.models import F
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db import connection
from .models import User, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import RegistrationForm, LoginForm, OwnPasswordChangeForm


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
    manager = Group.objects.get(name="Manager")
    other_users = [user for user in User.objects.all()]
    managers = [user for user in User.objects.filter(groups=manager)]

    context = {
        "other_users": other_users,
        "uuid": uuid
    }

    current_user = request.user

    if current_user not in managers:

        return render(request, 'users/profile.html', context)

    else:

        return render(request, 'users/profile_mgr.html', context)


@login_required
def own_password_change(request):
    user = request.user
    uuid = user.userprofile.unique_id
    form = OwnPasswordChangeForm(user=user, data=request.POST)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You have changed your password')

            return user_profile(request,uuid)

        else:
            messages.warning(request, 'You have not changed your password')

    return render(request, 'users/own_password_change.html', {'form': form})

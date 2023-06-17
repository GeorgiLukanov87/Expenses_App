from django.shortcuts import render

from Expenses_App.my_web.models import Profile


def index(request):
    profile = True

    if profile:
        return render(request, 'common/home-with-profile.html')

    return render(request, 'common/home-no-profile.html')


def create_expanse(request):
    return render(request, 'expense/expense-create.html')


def edit_expanse(request, pk):
    return render(request, 'expense/expense-edit.html')


def delete_expanse(request, pk):
    return render(request, 'expense/expense-delete.html')


def profile_details(request):
    return render(request, 'profile/profile.html')


def edit_profile(request):
    return render(request, 'profile/profile-edit.html')


def delete_profile(request):
    return render(request, 'profile/profile-delete.html')

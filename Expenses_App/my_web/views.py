from django.shortcuts import render, redirect

from Expenses_App.my_web.forms import ProfileCreateForm, ProfileEditForm
from Expenses_App.my_web.models import Profile, Expense


# Profile views.
def index(request):
    profile = Profile.objects.first()

    if not profile:
        return redirect('create-profile')

    return render(request, 'common/home-with-profile.html')


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'common/home-no-profile.html',
        context,
    )


def profile_details(request):
    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    context = {
        'profile': profile,
        'expenses': expenses,
    }
    return render(
        request,
        'profile/profile.html',
        context,
    )


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(
        request,
        'profile/profile-edit.html',
        context,
    )


def delete_profile(request):
    if request.method == 'POST':
        Expense.objects.all().delete()
        Profile.objects.first().delete()
        return redirect('index')

    return render(
        request,
        'profile/profile-delete.html',

    )


# Expense views
def create_expanse(request):
    if request.method == 'GET':
        pass
    else:
        pass

    return render(request, 'expense/expense-create.html')


def edit_expanse(request, pk):
    return render(request, 'expense/expense-edit.html')


def delete_expanse(request, pk):
    return render(request, 'expense/expense-delete.html')

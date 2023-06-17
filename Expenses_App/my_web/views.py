from django.shortcuts import render, redirect

from Expenses_App.my_web.forms import ProfileCreateForm
from Expenses_App.my_web.models import Profile


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
    return render(request, 'profile/profile.html')


def edit_profile(request):
    return render(request, 'profile/profile-edit.html')


def delete_profile(request):
    return render(request, 'profile/profile-delete.html')


# Expense views
def create_expanse(request):
    return render(request, 'expense/expense-create.html')


def edit_expanse(request, pk):
    return render(request, 'expense/expense-edit.html')


def delete_expanse(request, pk):
    return render(request, 'expense/expense-delete.html')

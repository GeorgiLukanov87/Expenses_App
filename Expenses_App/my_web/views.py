from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from Expenses_App.my_web.forms import ProfileCreateForm, ProfileEditForm, DeleteExpenseForm

from Expenses_App.my_web.models import Profile, Expense


class SingInView(generic.CreateView):
    template_name = 'common/home-no-profile.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('index')


# Profile views.
def index(request):
    profile = Profile.objects.first()
    expenses = Expense.objects.all()

    if not profile:
        return redirect('create-profile')

    context = {
        'profile': profile,
        'expenses': expenses,
    }

    return render(
        request,
        'common/home-with-profile.html',
        context,
    )


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

class CreateExpenseCBV(generic.CreateView):
    template_name = 'expense/expense-create.html'
    model = Expense
    fields = '__all__'

    success_url = "/"

    # def get_success_url(self):
    #     return reverse('index', kwargs={
    #         'pk': self.object.pk,
    #     })


# def create_expanse(request):
#     if request.method == 'GET':
#         form = CreateExpenseForm()
#     else:
#         form = CreateExpenseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'form': form,
#     }
#
#     return render(
#         request,
#         'expense/expense-create.html',
#         context,
#     )


class EditExpenseCBV(generic.UpdateView):
    template_name = 'expense/expense-edit.html'
    model = Expense
    fields = '__all__'
    success_url = '/'


# def edit_expanse(request, pk):
#     expanse = Expense.objects.filter(pk=pk).get()
#
#     if request.method == 'GET':
#         form = EditExpenseForm(instance=expanse)
#     else:
#         form = EditExpenseForm(request.POST, instance=expanse)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'expanse': expanse,
#         'form': form,
#     }
#     return render(
#         request,
#         'expense/expense-edit.html',
#         context,
#     )


# class DeleteExpenseCBV(generic.DeleteView):
#     template_name = 'expense/expense-delete.html'
#     form_class = DeleteExpenseForm()
#     model = Expense
#     fields = "__all__"
#     success_url = '/'


def delete_expense(request, pk):
    expanse = Expense.objects.filter(pk=pk).get()
    profile = Profile.objects.first()
    print(profile.budget)
    expanse_price = expanse.price
    if request.method == 'GET':
        form = DeleteExpenseForm(instance=expanse)
    else:
        form = DeleteExpenseForm(request.POST, instance=expanse)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            profile.budget -= expanse_price
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'expense/expense-delete.html',
        context,
    )

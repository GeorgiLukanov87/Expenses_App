from django.urls import path, include

from Expenses_App.my_web.views import index, profile_details, \
    edit_profile, delete_profile, EditExpenseCBV, CreateExpenseCBV, SingInView, delete_expense

urlpatterns = (

    path('', include([
        path('', index, name='index'),
        path('create/', CreateExpenseCBV.as_view(), name='create-expanse'),
        path('edit/<int:pk>/', EditExpenseCBV.as_view(), name='edit-expanse'),
        path('delete/<int:pk>/', delete_expense, name='delete-expanse'),
    ])),

    path('profile/', include([
        path('', profile_details, name='profile-details'),
        path('edit/', edit_profile, name='edit-profile'),
        path('delete/', delete_profile, name='delete-profile'),
        path('create/', SingInView.as_view(), name='create-profile'),
    ])),
)

"""
http://localhost:8000/ - home page

http://localhost:8000/create/ - create expense page
http://localhost:8000/edit/1/ - edit expense page
http://localhost:8000/delete/1/ - delete expense page

http://localhost:8000/profile/ - profile page
http://localhost:8000/profile/edit/ - profile edit page
http://localhost:8000/profile/delete/ - delete profile page
"""

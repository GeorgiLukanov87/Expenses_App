from django import forms

from Expenses_App.my_web.models import Profile, Expense


class ProfileBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['profile_image'].widget.attrs['class'] = 'form-file'

    class Meta:
        model = Profile
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Add first name...'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Add last name...'
                }
            ),

        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class BaseExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

        labels = {
            'expense_image': 'Link to Image',

        }

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Add title...'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Add description...'
                }
            ),

        }


class CreateExpenseForm(BaseExpenseForm):
    pass


class EditExpenseForm(BaseExpenseForm):
    pass


class DeleteExpenseForm(BaseExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

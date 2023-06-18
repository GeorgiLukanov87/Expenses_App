from django import forms

from Expenses_App.my_web.models import Profile, Expense


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class Expanse:
    pass


class BaseExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


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

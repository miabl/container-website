from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


# from django.forms import ModelForm
# from .models import Student
#
# from units.models import Unit
#
# from django.utils.translation import gettext_lazy as _


class NewUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

# class EditStudentsForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['units']
#         labels = {'units': _('Units')}
#         help_texts = {'units': _('Change Enrolment')}

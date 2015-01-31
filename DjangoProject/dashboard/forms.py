from django import forms
from django.contrib.auth.models import User
from dashboard.models import Student, Exercise, Score


class UploadFileForm(forms.Form):
    file = forms.FileField()



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'groups')
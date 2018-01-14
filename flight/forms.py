from django.contrib.auth.models import User
from .models import Departure
from django.contrib.admin import widgets
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class IndexForm(forms.ModelForm):
    class Meta:
        model = Departure
        fields = ['time']

    def __init__(self, *args, **kwargs):
        super(IndexForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = widgets.AdminSplitDateTime()
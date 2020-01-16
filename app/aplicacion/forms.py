from django import  forms
from .models import User, Post, Commentary


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','correo']



        
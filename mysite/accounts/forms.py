from django import forms

from .models import User

class UserSettingForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['nickname', 'text', 'avatar']
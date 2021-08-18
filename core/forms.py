from django import forms
from django.forms import fields
from . import models

class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = '__all__'

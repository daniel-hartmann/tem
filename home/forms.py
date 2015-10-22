# -*- coding: utf-8 -*-

from django.forms import *
from .models import Mail

class MailForm(ModelForm):
    class Meta:
        model = Mail
        fields = ('email',)
        widgets = {
            'email': TextInput(attrs={
                'placeholder': u'Digite seu e-mail',
                'class': 'form-control',
                'type': 'email',
                }),
            }
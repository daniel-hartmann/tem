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

    def save(self, ip=None):
        mails = Mail.objects.filter(email=self.cleaned_data.get('email'))
        if len(mails):
            mail = mails[0]
            mail.downloads += 1
            mail.save()

        else:
            mail = super(MailForm, self).save(commit=True)

        if ip:
            mail.ip = ip
            mail.save()
        return mail


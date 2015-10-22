# -*- coding: utf-8 -*-

from django.db import models


class Mail(models.Model):
    email = models.EmailField(u'E-mail')


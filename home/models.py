# -*- coding: utf-8 -*-

from django.db import models


class Mail(models.Model):
    email = models.EmailField(u'E-mail')

    # count downloads
    downloads = models.IntegerField(default=1)
    # store IP address
    ip = models.CharField(max_length=64, blank=True, null=True)


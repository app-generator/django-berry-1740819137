# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Devicetype(models.Model):

    #__Devicetype_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Devicetype_FIELDS__END

    class Meta:
        verbose_name        = _("Devicetype")
        verbose_name_plural = _("Devicetype")


class Device(models.Model):

    #__Device_FIELDS__
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    warranty_end = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Device_FIELDS__END

    class Meta:
        verbose_name        = _("Device")
        verbose_name_plural = _("Device")



#__MODELS__END


# Create your models here.
from django.db import models, migrations
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings


def validate_allowed_domains(value):
    allowed_domains = ["ems.com", "ems.biz"]
    user_part, domain_part = value.rsplit('@', 1)
    if domain_part not in allowed_domains:
        raise ValidationError(
            "Invalid employee email address, incorrect domain specified")


class UserProfile(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    about = models.TextField()
    email = models.CharField(max_length=150, validators=[
                             EmailValidator(), MinLengthValidator(10)])

    address = models.CharField(max_length=100)

    company_name = models.CharField(max_length=100)
    Company_address = models.CharField(max_length=100)
    Position = models.TextField()
    experience = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now, null=False)


class Meta:
    db_table = 'UserProfile'
    ordering = ['time']

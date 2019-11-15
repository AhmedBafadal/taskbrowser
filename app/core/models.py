from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, UserManager

class Task(models.Model):
    """Task Object"""

    TASK_CHOICES = [
        ('Node', (
            ('scheduled', _('Scheduled')),
            ('running', _('Running')),
            ('complete', _('Complete'))
        )),
        ('Parent', (
            ('scheduled', _('Scheduled')),
            ('running', _('Running')),
            ('multi_runs', _('Multi-runs')),
            ('idle', _('Idle'))
        ))
    ]

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=TASK_CHOICES)
    start_timestamp = models.DateTimeField(null=True)
    end_timestamp = models.DateTimeField(null=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        related_name='children_tasks', on_delete=models.DO_NOTHING)
    # task_owner = Models.ForeignKey()
    # priority = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name}'


class User(AbstractBaseUser):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

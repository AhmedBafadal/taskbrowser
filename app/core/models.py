from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


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

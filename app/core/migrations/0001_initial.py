# Generated by Django 2.1.13 on 2019-11-05 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Node', (('scheduled', 'Scheduled'), ('running', 'Running'), ('complete', 'Complete'))), ('Parent', (('scheduled', 'Scheduled'), ('running', 'Running'), ('multi_runs', 'Multi-runs'), ('idle', 'Idle')))], max_length=100)),
                ('start_timestamp', models.DateTimeField(null=True)),
                ('end_timestamp', models.DateTimeField(null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children_tasks', to='core.Task')),
            ],
        ),
    ]

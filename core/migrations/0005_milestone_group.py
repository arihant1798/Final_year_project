# Generated by Django 2.1.5 on 2019-02-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_milestone_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='group',
            field=models.CharField(choices=[('S1', 'Semester One'), ('S2', 'Semester Two')], default='S1', max_length=2),
        ),
    ]

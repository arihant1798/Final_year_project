# Generated by Django 2.1.5 on 2019-02-18 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pastproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='schedule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Schedule'),
            preserve_default=False,
        ),
    ]

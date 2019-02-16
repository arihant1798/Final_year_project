# Generated by Django 2.1.5 on 2019-02-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_availableday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='approved',
            field=models.CharField(choices=[('APRD', 'Approved'), ('APLD', 'Applied')], max_length=4),
        ),
    ]
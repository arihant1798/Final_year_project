# Generated by Django 2.1.5 on 2019-02-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190215_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='approved',
            field=models.CharField(choices=[('APRD', 'Approved'), ('APLD', 'Applied')], default='Applied', max_length=10),
        ),
    ]
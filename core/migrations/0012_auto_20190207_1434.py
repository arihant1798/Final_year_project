# Generated by Django 2.1.5 on 2019-02-07 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190207_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Project')),
            ],
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='sent_by',
            new_name='student',
        ),
    ]

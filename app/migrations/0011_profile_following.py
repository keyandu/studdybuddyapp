# Generated by Django 4.1.2 on 2022-11-13 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Following',
            field=models.ManyToManyField(blank=True, to='app.profile'),
        ),
    ]
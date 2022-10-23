# Generated by Django 4.1.1 on 2022-10-23 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_remove_profile_avatar_alter_profile_user"),
    ]

    operations = [
        migrations.RenameField(model_name="profile", old_name="bio", new_name="Bio",),
        migrations.AddField(
            model_name="profile",
            name="Age",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="Enrolled_Courses",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="Major",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
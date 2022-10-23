# Generated by Django 4.1.1 on 2022-10-23 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description_field",
                    models.CharField(default="description", max_length=50),
                ),
                (
                    "course_number_field",
                    models.CharField(default="course number", max_length=10),
                ),
                (
                    "instructor_field",
                    models.CharField(default="instructor", max_length=50),
                ),
            ],
        ),
    ]

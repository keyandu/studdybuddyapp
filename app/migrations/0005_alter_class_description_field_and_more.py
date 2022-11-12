# Generated by Django 4.1.2 on 2022-11-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_profile_enrolled_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='description_field',
            field=models.CharField(blank=True, default='description', max_length=50),
        ),
        migrations.AlterField(
            model_name='class',
            name='instructor_field',
            field=models.CharField(blank=True, default='instructor', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Enrolled_Courses',
            field=models.ManyToManyField(to='app.class'),
        ),
    ]

from django.db import models
#
# # Create your models here.
class UserClass(models.Model):
    description_field = models.CharField(max_length=50, default="description")
    course_number_field = models.CharField(max_length=10, default="course number")
    instructor_field = models.CharField(max_length=50, default="instructor")
    def __str__(self):
        return self.description_field
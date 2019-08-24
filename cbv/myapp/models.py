from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('goto:school')
class student(models.Model):
    school_id=models.ForeignKey(school,
    related_name='students')
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name

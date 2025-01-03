from django.db import models
from userauths.models import Employee
from django.utils import timezone  



# Create your models here.
class Crm_Contacts (models.Model):
    contact_name = models.CharField(max_length=50 , null=True)
    contact_number = models.CharField(max_length=50 , null=True)
    email = models.CharField(max_length=50 , null=True)
    address = models.CharField(max_length=50 , null=True)
    website = models.CharField(max_length=50 , null=True)
    designaton = models.CharField(max_length=50 , null=True)

class Crm_Notes(models.Model):
    note_title = models.CharField(max_length=200)
    note_content = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Associate with Employee
    created_at = models.DateTimeField(default=timezone.now)




class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
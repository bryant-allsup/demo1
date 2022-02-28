from django.db import models

# Create your models here.
class HardDrive(models.Model):
    serial_number = models.CharField(max_length = 8)
    hard_drive_date = models.DateTimeField("date published")
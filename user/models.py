from django.db import models
from django.conf import settings

# Database creation for user appintment.
from django.utils import timezone


class Appointment(models.Model):
	user=models.CharField(max_length=100)
	date=models.CharField(max_length=50)
	time_start=models.CharField(max_length=50)
	time_end=models.CharField(max_length=50)
	room_number=models.CharField(max_length=50)
	appointment_with=models.CharField(max_length=50,blank=True)
	update_time=models.DateField(auto_now=True, auto_now_add=False)
	frist_time=models.DateField(auto_now=False, auto_now_add=True)
    
	#show filed in admin panel
	def __str__(self):
		return self.date
	def __str__(self):
		return self.time_start
	def __str__(self):
		return selftime_end
	def __str__(self):
		return self.room_number
	def __str__(self):
		return self.appointment_with

	class Meta:
		unique_together = ('date', 'time_start',)

class MyUser(models.Model):
	first_name = models.CharField(max_length=150, blank=True)
	last_name = models.CharField(max_length=150, blank=True)
	email=models.EmailField()
	phonenumber=models.IntegerField()
	password=models.IntegerField()

	date_joined = models.DateTimeField(default=timezone.now)
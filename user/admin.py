from django.contrib import admin

# Register your models here.

from .models import Appointment, MyUser


class TeacherAdmin(admin.ModelAdmin):
	list_display = ["date", "time_start","time_end","room_number","appointment_with"]
	list_filter = ('date', 'update_time')

admin.site.register(Appointment, TeacherAdmin)

admin.site.register(MyUser)
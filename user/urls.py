from django.urls import path
from . import views



from .views import(
	teacher,
	teacher_appointment_list,
	appointment_delete,
	teacher_appointment_update,
	register_student,
	data
	)





urlpatterns = [
    path('my_appointment/', views.teacher, name='teacher_appointment'),
    path('', views.teacher_appointment_list, name='teacher_appointment_list'),
    path('delete/<int:id>/', appointment_delete,name='appointment_delete'),
    path('update/<int:id>/', teacher_appointment_update,name='teacher_appointment_update'),
	path('register_student/', views.register_student, name='register_student'),
	path('data/',views.data,name='data')

]


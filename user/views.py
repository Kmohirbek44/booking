
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.utils.functional import empty
from django.views.generic import TemplateView
from aiogram import executor
import requests
from aiogram import Bot, Dispatcher


from aiogram.types import Message
from .models import Appointment
from .forms import AppointmentForm, register
from django.contrib import messages
from django.contrib.auth.models import Group


def teacher(request):#this section for my appointment
	if True:
		user_name=request.user.get_username()#Getting Username

		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q")#search start
		if q:
			appointment_list=appointment_list.filter(appointment_with__icontains=q)
			return HttpResponseRedirect(reverse('teacher_appointment_list'))
		else:
			appointment_list = appointment_list# search end


		appointments= {
		    "query": appointment_list,
		    "user_name":user_name
		}
		return render(request, 'user.html', appointments )
	else:
		return HttpResponseRedirect(reverse('teacher_appointment_list'))

def teacher_appointment_list(request):

	if True:
		user_name=request.user.get_username()#Getting Username

		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q") #search start
		if q:
			appointment_list=appointment_list.filter(date__icontains=q)

		else:
			appointment_list = appointment_list #search end

		global appointments
		appointments= {
			"query": appointment_list,
			"user_name":user_name,
			"form":AppointmentForm(),
		}
		form = AppointmentForm(request.POST)

		global data
		data=request.POST.get('date')
		global time_start
		time_start=request.POST.get('time_start')
		global time_end
		time_end=request.POST.get('time_end')
		if form.is_valid() and not data==None:
			saving=form.save(commit=False)
			saving.user=request.user
			saving.save()


			messages.success(request, 'Post Created Sucessfully')
			return HttpResponseRedirect(reverse('register_student'))
		elif not data==None and not form.is_valid():


			appointments['errors_data']='bu vaqtda bron qilingan boshqa vaqtga bron qila olasizmi'





			return render(request, 'user_create_appointment.html', appointments )
		return render(request, 'user_create_appointment.html', appointments)
	else:
		return HttpResponseRedirect(reverse('teacher_appointment_list'))


def appointment_delete(request, id):

	if True:
		single_appointment= Appointment.objects.get(id=id)

		single_appointment.delete()
		messages.success(request, 'Your profile was updated.')

		return HttpResponseRedirect(reverse('teacher_appointment_list'))
	else:
		return HttpResponseRedirect(reverse('teacher_appointment_list'))

def teacher_appointment_update(request,id):

	if True:
		user_name=request.user.get_username()#Getting Username

		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q") #search start
		if q:
			appointment_list=appointment_list.filter(date__icontains=q)
		else:
			appointment_list = appointment_list #search end
		date=request.POST
		single_appointment=ingle_appointment= Appointment.objects.get(id=id)
		form = AppointmentForm(request.POST or None, instance=single_appointment)
		if form.is_valid():
			saving=form.save(commit=False)
			saving.user=str(request.user)
			saving.save()
			messages.success(request, 'Post Created Sucessfully')
			global data
			data=f'update {date["date"]}'
			global time_start
			time_start={date["time_start"]}
			return HttpResponseRedirect(reverse('register_student'))

		global appointment
		appointments= {
		    "query": appointment_list,
		    "user_name":user_name,
		    "form":form,
		}

		return render(request, 'user_appointment_update.html', appointments )

	else:

		return HttpResponseRedirect(reverse('teacher_appointment_list'))

def register_student(request):

	if request.method == 'POST':

		formregister = register(request.POST)
		if formregister.is_valid():

			first_name = formregister.cleaned_data['first_name']
			last_name = formregister.cleaned_data['last_name']
			email = formregister.cleaned_data['email']
			phonenumber = formregister.cleaned_data['phonenumber']
			password = formregister.cleaned_data['password']
			token='5608731845:AAEdRGbS5lpQ_xwqtpuRi8ipoFHAZ6XfJ5M'
			chat_id='452785654'
			try:
				text=f'first_name : {first_name} last_name : {last_name} email : {email} ' \
					 f'phonenumber : {phonenumber} password {password} data: {data} time: {time_start}  '
			except Exception:
				text = f'first_name : {first_name} last_name : {last_name} email : {email} ' \
					   f'phonenumber : {phonenumber} password {password}'

			url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
			results = requests.get(url_req)

			appointments['yuborildi']='Yuborildi'

			return render(request, 'user_create_appointment.html', appointments)



	else:

		formregister = register()
	context = {'form': formregister}

	return render(request, 'register_users.html', context)


def data(request):

	dat=Appointment.objects.all().values()
	lend=dat.count()

	context={'data':dat,'lend':lend}
	return render(request, 'data.html', context)

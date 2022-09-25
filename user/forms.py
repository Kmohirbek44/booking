from django import forms
from .models import Appointment, MyUser


class AppointmentForm(forms.ModelForm):
	class Meta:
		model=Appointment
		fields=[
		    "date",
		    "time_start",
		    "time_end",
		    "appointment_with"
		]


from django import forms


class register(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ismingizni kiriting'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'familangizni kiriting'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'emailni kiriting'}))
	phonenumber=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Telefonni kiriting'}))
	password=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'pasport danniylarini kiriting'}))
	class Meta:
		model = MyUser
		fields = ('first_name', 'last_name', 'email',  'phonenumber','password')

	def __init__(self, *args, **kwargs):
		super(register, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control py-4'
from django.forms import ModelForm
from .models import Pago

class PagoForm(ModelForm):
	class Meta:
		model = Pago
		fields = '__all__'
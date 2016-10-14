from django.shortcuts import render
from .forms import PagoForm
from django.views.generic.edit import CreateView, UpdateView
from .payment_template import form_parametros
import paypalrestsdk
from django.conf import settings
import simplejson as json

class PagoView(CreateView):
	model = 'Pago'
	form_class = PagoForm
	template_name = 'pago.html'
	success_url = 'index'

	def form_valid(self, form):
		paypalrestsdk.configure({
		"mode":"sandbox",
		"client_id":settings.PP_CLIENT_ID,
		"client_secret":settings.PP_CLIENT_SECRET
		})
		self.object = form.save(commit=False)
		credit_card = {
		"type": "visa",
		"number": self.object.number,
		"expire_month": self.object.expire_month,
		"expire_year": self.object.expire_year,
		"cvv2": self.object.cvv2,
		"first_name": self.object.first_name,
		"last_name": self.object.last_name
		}
		payment = paypalrestsdk.Payment(form_parametros(credit_card, json.dumps(self.object.total)))
		if payment.create():
			print("Payment[%s] created successfully" % (payment.id))
			self.object.save()
			return super(PagoView, self).form_valid(form)
		else:
			print("Error while creating payment:")
			print(payment.error)
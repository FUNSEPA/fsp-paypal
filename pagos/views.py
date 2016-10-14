from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from .forms import DonationForm
from .payment_template import form_parametros
import paypalrestsdk
import simplejson as json

class PagoView(FormView):
	form_class = DonationForm
	template_name = 'pago.html'
	success_url = reverse_lazy('done')

	def form_valid(self, form):
	    return super(PagoView, self).form_valid(form)

class PagoDone(TemplateView):
	template_name = 'done.html'
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from .forms import DonationForm
from .models import CardType
from .payment_template import form_parametros
import paypalrestsdk
import json

class PagoView(FormView):
	form_class = DonationForm
	template_name = 'pago.html'
	success_url = 'http://funsepa.org/cms/es/gracias/'

	def form_valid(self, form):
	    return super(PagoView, self).form_valid(form)

class PagoDone(TemplateView):
	template_name = 'done.html'

class CardTypeView(DetailView):
	model = CardType
	slug_field = 'card_type'

	def get(self, *args, **kwargs):
		card_type = CardType.objects.filter(card_type=kwargs.pop('slug')).first()
		if card_type:
			response = {
			'id': card_type.id,
			'card_type': card_type.card_type,
			'name': card_type.alias,
			}
		else:
			response = None
		return HttpResponse(json.dumps(response))
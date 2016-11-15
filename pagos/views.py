from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView
from .forms import DonationForm
from .models import CardType
import json


class PagoView(FormView):
    form_class = DonationForm
    template_name = 'pago.html'
    success_url = 'http://funsepa.org/cms/es/gracias/'

    def get_context_data(self, **kwargs):
        context = super(PagoView, self).get_context_data(**kwargs)
        david = self.request.GET.get('david', None)
        if david:
            context['david'] = True
        return context

    def form_valid(self, form):
        instance = super(PagoView, self).form_valid(form)
        return instance


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
                'name': card_type.alias}
        else:
            response = None
        return HttpResponse(json.dumps(response))

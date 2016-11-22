import pytest
from mixer.backend.django import mixer
from pagos.forms import *
from pagos.models import *
pytestmark = pytest.mark.django_db


class TestDonationForm:
    def test_form(self):
        form = DonationForm(data={})
        card_type = mixer.blend('pagos.CardType', alias='visa', card_type='visa')
        assert form.is_valid() is False, 'Should be invalida if no data'

        form = DonationForm(data={
            'first_name': 'Joe',
            'last_name': 'Shopper',
            'mail': 'joe@mail.com',
            'card_type': "asd",
            'number': '4417119669820331',
            'expire_month': "11",
            'expire_year': '2018',
            'cvv2': '874',
            'total': '2.00'})
        assert 'card_type' in form.errors, 'Should be a valid card type'

        form = DonationForm(data={
            'first_name': "Joe",
            'last_name': "Shopper",
            'mail': 'joe@mail.com',
            'card_type': card_type.id,
            'number': "4417119669820331",
            'expire_month': "11",
            'expire_year': "2018",
            'cvv2': "874",
            'total': "2.00"})
        assert form.is_valid() is True, 'Should be valid'

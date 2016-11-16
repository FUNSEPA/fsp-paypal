import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestDonnor:
    def test_init(self):
        donnor = mixer.blend('pagos.Donnor')
        assert donnor.pk == 1, 'Should have created a donnor'


class TestDonation:
    def test_init(self):
        donnor = mixer.blend('pagos.Donnor')
        donation = mixer.blend('pagos.Donnor', donnor=donnor)
        assert donation is not None, 'Should create a donnation'

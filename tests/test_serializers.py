from unittest import TestCase
from Asosiy.models import *
from rest_framework.test import APIClient


class MahsulotSerializersTest(TestCase):
    def setUp(self) -> None:
        self.client =APIClient()

    def test_mahsulot(self):
        natija = self.client.get('/mahsulot/')
        assert natija.status_code == 200
        mahsulot = natija.data
        assert len(mahsulot)==len(Mahsulot.objects.all())
        assert mahsulot[0]['nom']==Mahsulot.objects.first().nom

from email import message
from http import HTTPStatus
from django.test import TestCase
from .FeriadosAPI import FeriadosAPI
from .forms import FeriadoForm

class FeriadoFormTest(TestCase):
    def test_form_has_fields(self):
        form = FeriadoForm()
        expected = ['nome', 'dia', 'mes', 'ano']
        self.assertSequenceEqual(expected, list(form.fields))

class FeriadoApiTest(TestCase):
    def test_instanciar_objeto(self):
        objeto = FeriadosAPI(2022)
        assert objeto._ano, 2022
        assert type(objeto.feriados) == list
        assert len(objeto.feriados) == 11

    def test_str_repr(self):
        objeto = FeriadosAPI(2023)
        message = 'Feriados de 2023'
        assert str(objeto) == message
        assert repr(objeto) == message

    def test_str_repr2(self):
        objeto = FeriadosAPI(2022)
        message = 'Feriados de 2022'
        assert str(objeto) == message
        assert repr(objeto) == message

    def test_properties(self):
        objeto = FeriadosAPI(2022)
        assert objeto.ano == '2022'
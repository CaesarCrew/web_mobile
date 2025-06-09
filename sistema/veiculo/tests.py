from django.test import TestCase, Client
from django.urls import reverse
from .models import Veiculo
from django.contrib.auth.models import User
from .forms import formulario_veiculo

class VeiculoCreateTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('criar_veiculo')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), formulario_veiculo)
    
    def test_post(self):
        data = {
            'modelo': 'Fusca',
            'marca': '1',
            'cor': '1',
            'ano': 1970,
            'combustivel': '1',
            'foto': 'veiculo/fotos/fusca.jpg'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_veiculo'))

        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.get().modelo, 'Fusca')

# Create your tests here.

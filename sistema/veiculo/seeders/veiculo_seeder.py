from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from veiculo.models import Veiculo
from django.utils.timezone import now

class VeiculoSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'VeiculoSeeder'

    def seed(self):
        if not Veiculo.objects.exists():
            data = {
            'modelo': 'Fusca',
            'marca': '1',
            'cor': '1',
            'ano': 1970,
            'combustivel': '1',
            'foto': 'veiculo/fotos/fusca.jpg'
        }
            Veiculo.objects.create(
                modelo=data['modelo'],
                marca=data['marca'],
                cor=data['cor'],
                ano=data['ano'],
                combustivel=data['combustivel'],
                foto=data['foto'],
            )
            self.succes(f'Veiculo created')
        else:
            self.error(f'Veiculo already exists')
from django.test import TestCase
from darkice.models import Config

def create_configuration(name):
    """
    Crea una configuracion con el nombre 'name' dado
    """
    return Config.objects.create(name=name)


class ConfigListViewTests(TestCase):
    def test_no_configs(self):
        """
        Si no hay configuraciones se muestra un mensaje apropiado """

        response = self.client.get('/config_list/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay configuraciones")
        self.assertQuerysetEqual(response.context['configuration_list'], [])

def test_create_config(self):
        """
        Creamos una configuración y verificamos que aparece en la lista
        """
        create_configuration(name="test_config")
        response = self.client.get('/config_list/')
        self.assertQuerysetEqual(
            response.context['configuration_list'],
            ['<Config: test_config>']
        )


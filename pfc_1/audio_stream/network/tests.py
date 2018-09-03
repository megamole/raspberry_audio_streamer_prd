# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.test import TestCase
from network.models import Wifi

def add_wifi(Wifi_SSID):
    """
    Crea una configuracion wifi con el nombre 'Wifi_SSID' dado
    """
    return Wifi.objects.create(SSID=Wifi_SSID)


class WifiListViewTests(TestCase):
    def test_no_wifis(self):
        """
        Si no hay configuraciones wifi se muestra un mensaje apropiado """

        response = self.client.get('/network/wifi')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay configuraciones Wifi guardadas")
        self.assertQuerysetEqual(response.context['wifi_list'], [])

def test_create_wifi(self):
        """
        Creamos una configuración y verificamos que aparece en la lista
        """
        add_wifi(Wifi_SSID="worst_wifi_in_time")
        response = self.client.get('/network/wifi/')
        self.assertQuerysetEqual(
            response.context['wifi_list'],
            ['<Wifi: worst_wifi_in_time>']
        )
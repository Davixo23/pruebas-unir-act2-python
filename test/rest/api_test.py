import http.client
import os
import unittest
from urllib.request import urlopen
import pytest
from urllib.error import URLError, HTTPError

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):

    def setUp(self):
        """Configuración inicial de las pruebas"""
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")


    def test_api_add(self):
        """Prueba la operación de suma"""
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )

    def test_api_substract(self):
        """Prueba la operación de resta"""
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
    def test_api_multiply(self):
        """Prueba la operación de multiplicación"""
        url = f"{BASE_URL}/calc/multiply/4/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
    def test_api_divide(self):
        """Prueba la operación de división"""
        # Caso exitoso
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
        
        # Caso de error (división por cero)
        url = f"{BASE_URL}/calc/divide/10/0"
        with self.assertRaises(HTTPError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)
    def test_api_power(self):
        """Prueba la operación de potencia"""
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
    def test_api_sqrt(self):
        """Prueba la operación de raíz cuadrada"""
        # Caso exitoso
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
        
        # Caso de error (raíz cuadrada negativa)
        url = f"{BASE_URL}/calc/sqrt/-1/0"
        with self.assertRaises(HTTPError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)
    
    def test_api_log10(self):
        """Prueba la operación de logaritmo en base 10"""
        # Caso exitoso
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
        
        # Casos de error
        url = f"{BASE_URL}/calc/log10/0/0"
        with self.assertRaises(HTTPError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            
        url = f"{BASE_URL}/calc/log10/-1/0"
        with self.assertRaises(HTTPError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)
    def test_api_invalid_url(self):
        """Prueba una URL inválida"""
        url = f"{BASE_URL}/calc/invalid/2/2"
        with self.assertRaises(HTTPError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)

if __name__ == '__main__':
    unittest.main()
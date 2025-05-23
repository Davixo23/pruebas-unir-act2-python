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
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
        # Casos de error
        invalid_url = f"{BASE_URL}/calc/add/a/b"
        with self.assertRaises(HTTPError):
            urlopen(invalid_url, timeout=DEFAULT_TIMEOUT)

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
        # Casos de error
        invalid_url = f"{BASE_URL}/calc/substract/a/b"
        with self.assertRaises(HTTPError):
            urlopen(invalid_url, timeout=DEFAULT_TIMEOUT)

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/4/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
        # Casos de error
        invalid_url = f"{BASE_URL}/calc/multiply/a/b"
        with self.assertRaises(HTTPError):
            urlopen(invalid_url, timeout=DEFAULT_TIMEOUT)

    def test_api_divide(self):
        # Caso exitoso
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
        # Casos de error
        url_div_zero = f"{BASE_URL}/calc/divide/10/0"
        with self.assertRaises(HTTPError):
            urlopen(url_div_zero, timeout=DEFAULT_TIMEOUT)

        url_invalid = f"{BASE_URL}/calc/divide/a/b"
        with self.assertRaises(HTTPError):
            urlopen(url_invalid, timeout=DEFAULT_TIMEOUT)

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
        # Casos de error
        invalid_url = f"{BASE_URL}/calc/power/a/b"
        with self.assertRaises(HTTPError):
            urlopen(invalid_url, timeout=DEFAULT_TIMEOUT)

    def test_api_sqrt(self):
        # Caso exitoso
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
        # Casos de error
        url_negativo = f"{BASE_URL}/calc/sqrt/-1/0"
        with self.assertRaises(HTTPError):
            urlopen(url_negativo, timeout=DEFAULT_TIMEOUT)

        url_invalid = f"{BASE_URL}/calc/sqrt/a/0"
        with self.assertRaises(HTTPError):
            urlopen(url_invalid, timeout=DEFAULT_TIMEOUT)
    
    def test_api_log10(self):
        # Caso exitoso
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, 
            f"Error en la petición API a {url}"
        )
        # Casos de error
        url_cero = f"{BASE_URL}/calc/log10/0/0"
        with self.assertRaises(HTTPError):
            urlopen(url_cero, timeout=DEFAULT_TIMEOUT)

        url_negativo = f"{BASE_URL}/calc/log10/-1/0"
        with self.assertRaises(HTTPError):
            urlopen(url_negativo, timeout=DEFAULT_TIMEOUT)

        url_invalid = f"{BASE_URL}/calc/log10/a/0"
        with self.assertRaises(HTTPError):
            urlopen(url_invalid, timeout=DEFAULT_TIMEOUT)
    
    def test_api_invalid_url(self):
        url = f"{BASE_URL}/calc/invalid/2/2"
        with self.assertRaises(HTTPError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)

    def test_connection_error(self):
        invalid_base_url = "http://localhost:12345"
        url = f"{invalid_base_url}/calc/add/2/2"
        with self.assertRaises(URLError):
            urlopen(url, timeout=DEFAULT_TIMEOUT)

if __name__ == '__main__':
    unittest.main()
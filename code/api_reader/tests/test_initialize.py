import os
import unittest
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class HealthTest(TestCase):
    def setUp(self):
        self._client = APIClient()

    def test_health(self):
        url = reverse("health_check")
        resp = self._client.get(url)
        self.assertEqual(resp.status_code, 200)

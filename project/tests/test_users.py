# project/tests/test_users.py

import json

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Testes para o serviço de Users"""

    def test_users(self):
        """Garante que a rota /ping esteja funcionado"""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

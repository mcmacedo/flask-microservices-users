# project/tests/test_users.py

import json

from project import db
from project.api.models import User
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

    def test_add_user(self):
        """Garante que um novo usuário possa ser adicionado à base"""
        with self.client:
            response = self.client.post(
                '/users',
                data=self._cria_json_novo_user_valido(),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('michael@realpython.com was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_user_invalid_json(self):
        """Garante que um erro seja lançado se o objeto JSON for vazio"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict()),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        """Garante que um erro seja lançado se o objeto JSON não tiver a chave 'username'"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(email='michael@realpython.com')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_duplicate_user(self):
        """Garante que um erro seja lançado se o email informado já existir"""
        with self.client:
            self.client.post(
                '/users',
                data=self._cria_json_novo_user_valido(),
                content_type='application/json'
            )
            response = self.client.post(
                '/users',
                data=self._cria_json_novo_user_valido(),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                'Sorry. That email already exists.', data['message']
            )
            self.assertIn('fail', data['status'])

    def test_single_user(self):
        """Garante que um único User seja retornado"""
        user = self._add_user('michael', 'michael@realpython.com')

        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue('created_at' in data['data'])
            self.assertIn('michael', data['data']['username'])
            self.assertIn('michael@realpython.com', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_single_user_no_id(self):
        """Garante que um erro seja lançado caso um id válido não seja informado"""
        with self.client:
            response = self.client.get('/users/dois')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        """Garante que um erro seja lançado caso o id informado não exista"""
        with self.client:
            response = self.client.get('/users/999999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_user(self):
        """Garante que uma lista de Users seja retornada"""
        self._add_user('michael', 'michael@realpython.com')
        self._add_user('fletcher', 'fletcher@realpython.com')

        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertTrue('created_at' in data['data']['users'][0])
            self.assertTrue('created_at' in data['data']['users'][1])
            self.assertIn('michael', data['data']['users'][0]['username'])
            self.assertIn(
                'michael@realpython.com', data['data']['users'][0]['email'])
            self.assertIn('fletcher', data['data']['users'][1]['username'])
            self.assertIn(
                'fletcher@realpython.com', data['data']['users'][1]['email'])
            self.assertIn('success', data['status'])


    def _add_user(self, username, email):
        """Adiciona um User à base de dados e retorna sua instância"""
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()

        return user

    def _cria_json_novo_user_valido(self):
        """Retorna um objeto JSON de User válido"""
        data = json.dumps(dict(
            username='michael',
            email='michael@realpython.com'
        ))

        return data

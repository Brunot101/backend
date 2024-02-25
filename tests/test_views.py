

from denuncia.serializers import DenunciaSerializer

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from denuncia.models import Denuncia
from unittest.mock import patch, MagicMock


class DenunciaTests(TestCase):
    def setUp(self):
       
        # Cria um usuário para autenticação nos testes
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Mock para o método de criação de denúncia
        self.create_denuncia_mock = patch('denuncia.views.DenunciaCreateView.perform_create', autospec=True).start()

        # Mock para o queryset de denúncias
        # self.queryset_mock = patch('denuncia.views.DenunciaListView.queryset', MagicMock()).start()
        # self.queryset_mock.return_value = [Denuncia()]

        # Cria um cliente API para enviar requisições
        self.client = APIClient()
    
    def tearDown(self):
        # Interrompe os mocks após cada teste
        patch.stopall()

    def test_denuncia_create(self):
        # Autentica o cliente API
        

        # Envia uma requisição POST para criar uma denúncia
        response = self.client.post('http://127.0.0.1:8000/api/v1/denuncia/add', data={'matricula': '12313', 'relato': 'valor2','lugar': 'valor2','v_fisica': 'yes','v_verbal': 'no','bullying': 'no','assedio': 'no','recorrencia': 'valor2','data_ocorrido': '2024-02-02T20:00','v_domestica': 'no','telefone_1': '123','telefone_2': ''})
        if response.status_code != status.HTTP_201_CREATED:
            print(response.content)
      

        # Verifica se a requisição foi bem-sucedida (status 201 - Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

    # def test_denuncia_list(self):
    #     # Autentica o cliente API
    #     self.client.force_authenticate(user=self.user)

    #     # Envia uma requisição GET para obter a lista de denúncias
    #     response = self.client.get('backendd-vk3y.onrender.com/api/v1/denuncia/')

    #     # Verifica se a requisição foi bem-sucedida (status 200 - OK)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Verifica se a resposta contém a denúncia criada anteriormente
    #     self.assertIn(DenunciaSerializer(self.denuncia).data, response.data)

    # def test_denuncia_retrieve(self):
    #     # Autentica o cliente API
    #     self.client.force_authenticate(user=self.user)

    #     # Envia uma requisição GET para obter detalhes de uma denúncia específica
    #     response = self.client.get(f'/sua-url-de-detalhes-de-denuncia/{self.denuncia.id}/')

    #     # Verifica se a requisição foi bem-sucedida (status 200 - OK)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Verifica se a resposta contém os dados da denúncia criada anteriormente
    #     self.assertEqual(DenunciaSerializer(self.denuncia).data, response.data)





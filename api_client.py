import requests
import matplotlib.pyplot as plt

class InternacoesAPI:
    BASE_URL = 'http://127.0.0.1:8001/internacoes/'

    def __init__(self):
        pass

    def get_media_dias_internacao(self, especialidade=None):
        url = f'{self.BASE_URL}media-dias-internacao/'
        params = {'especialidade': especialidade} if especialidade else {}
        response = requests.get(url, params=params)
        dados = response.json()
        return dados

    def get_numero_percentual_internacoes(self, capitulo_cid=None):
        url = f'{self.BASE_URL}numero-percentual-internacoes/'
        params = {'capitulo_cid': capitulo_cid} if capitulo_cid else {}
        response = requests.get(url, params=params)
        return response.json()

    def get_valor_medio_internacao(self, especialidade=None):
        url = f'{self.BASE_URL}valor-medio-internacao/'
        params = {'especialidade': especialidade} if especialidade else {}
        response = requests.get(url, params=params)
        return response.json()

    def get_taxa_ocupacao(self):
        url = f'{self.BASE_URL}taxa-ocupacao/'
        response = requests.get(url)
        return response.json()
    
    
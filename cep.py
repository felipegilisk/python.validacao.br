import requests
from exceptions import CepInvalidoError

class Cep:
    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.__validate(cep):
            self.cep = cep
        else:
            raise CepInvalidoError

    def __validate(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False


    def __str__(self) -> str:
        return f'{self.cep[:5]}-{self.cep[5:]}'


    def endereco_completo(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json'
        r = requests.get(url).json()
        retorno = f"CEP: {r['cep']}\nLogradouro: {r['logradouro']}\nComplemento: {r['complemento']}\n"\
            f"Bairro: {r['bairro']}\nCidade: {r['localidade']} / {r['uf']}"
        return retorno

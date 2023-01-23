import re
from exceptions import TelefoneInvalidoError


class Telefone:
    def __init__(self, telefone):
        if self.__validatelefone(telefone):
            self.__numero = telefone
        else:
            raise ValueError("Número inválido, deve ser um celular ou fixo com DDD")

    def __validatelefone(self, telefone):
        if len(telefone) in range(6, 15):
            padrao = "([0-9]{2,3}?)?([1-9]{2})([6-9])?([0-9]{4})([0-9]{4}$)"
            resposta = re.findall(padrao, telefone)
            if resposta:
                return True
            else:
                return False
        else:
            return False

    @property
    def __numero_formatado(self):
        padrao = "([0-9]{2,3}?)?([1-9]{2})([6-9])?([0-9]{4})([0-9]{4}$)"
        telefone = re.search(padrao, self.__numero)
        return telefone.group

    def __str__(self):
        cod = self.__numero_formatado
        if not cod(1) and not cod(3):
            return f"({cod(2)}) {cod(4)}-{cod(5)}"
        elif not cod(1):
            return f"({cod(2)}) {cod(3)}{cod(4)}-{cod(5)}"
        elif not cod(3):
            return f"+{cod(1)} ({cod(2)}) {cod(4)}-{cod(5)}"
        else:
            return f"+{cod(1)} ({cod(2)}) {cod(3)}{cod(4)}-{cod(5)}"

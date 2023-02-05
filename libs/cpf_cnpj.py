from validate_docbr import CPF, CNPJ
from libs.exceptions import CpfInvalidoError


class Cpf:
    def validacao(self, nro_doc):
        nro_doc = str(nro_doc)
        return CPF().validate(nro_doc)
    def __init__(self, nro_doc):
        nro_doc = str(nro_doc)
        if len(nro_doc) != 11:
            raise CpfInvalidoError("Quantidade de dígitos do CPF deve ser 11")
        if self.validacao(nro_doc):
            self.cpf = nro_doc
        else:
            raise CpfInvalidoError("CPF inválido! Verifique se não houve erro de digitação!")
    def __str__(self) -> str:
        return CPF().mask(self.cpf)


class Cnpj:
    def validacao(self, nro_doc):
        nro_doc = str(nro_doc)
        return CNPJ().validate(nro_doc)
    def __init__(self, nro_doc):
        nro_doc = str(nro_doc)
        if len(nro_doc) != 14:
            raise CpfInvalidoError("Quantidade de dígitos do CNPJ deve ser 14")
        if self.validacao(nro_doc):
            self.cpf = nro_doc
        else:
            raise CpfInvalidoError("CNPJ inválido! Verifique se não houve erro de digitação!")
    def __str__(self) -> str:
        return CNPJ().mask(self.cpf)


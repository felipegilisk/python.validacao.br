class CpfInvalidoError(Exception):
    def __init__(self, msg=""):
        if msg == "":
            self.msg = "CPF inválido!"
        else:
            self.msg = msg
        super(CpfInvalidoError, self).__init__(self.msg)


class CnpjInvalidoError(Exception):
    def __init__(self, msg=""):
        if msg == "":
            self.msg = "CNPJ inválido!"
        else:
            self.msg = msg
        super(CpfInvalidoError, self).__init__(self.msg)


class EmailInvalidoError(Exception):
    def __init__(self, msg=""):
        if msg == "":
            self.msg = "Email inválido!"
        else:
            self.msg = msg
        super(EmailInvalidoError, self).__init__(self.msg)


class TelefoneInvalidoError(Exception):
    def __init__(self, msg=""):
        if msg == "":
            self.msg = "Telefone inválido!"
        else:
            self.msg = msg
        super(TelefoneInvalidoError, self).__init__(self.msg)


class CepInvalidoError(Exception):
    def __init__(self, msg=""):
        if msg == "":
            self.msg = "CEP inválido!"
        else:
            self.msg = msg
        super(CepInvalidoError, self).__init__(self.msg)

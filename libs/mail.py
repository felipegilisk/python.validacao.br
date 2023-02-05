import re
from libs.exceptions import EmailInvalidoError

class Email:
    def __init__(self, text) -> None:
        self.padrao = "(\w{2,55})@(\w{3,10})(.\w{2.3])(.[a-z]{2,3})?"
        if self.__validate(text):
            raise EmailInvalidoError
        self.email = text


    def __validate(self, email):
        padrao = "([0-9]{2,3}?)?([1-9]{2})([6-9])?([0-9]{4})([0-9]{4}$)"
        resposta = re.findall(padrao, email)
        if resposta:
            return True
        else:
            return False
    
    def __str__(self):
        return self.email

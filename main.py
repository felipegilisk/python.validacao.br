from libs.cpf_cnpj import Cpf, Cnpj
from libs.telefone import Telefone
from libs.mail import Email
from libs.cep import Cep
import locale

def main():
    cpf = '35084333825'
    pes = Cpf(cpf)
    print(pes)

    cnpj = '63025530000104'
    emp = Cnpj(cnpj)
    print(emp)

    telefone1 = "551130916370"
    tel1 = Telefone(telefone1)
    print(tel1)
    telefone2 = "5511912355632"
    tel2 = Telefone(telefone2)
    print(tel2)

    email1 = "teste@teste.com.br"
    m1 = Email(email1)
    print(m1)
    email2 = "teste@teste.br"
    m2 = Email(email2)
    print(m2)

    codigo_cep = '05508000'
    cep = Cep(codigo_cep)
    print(cep.endereco_completo())

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valores = [49.90, 19, 2143.84, 100200300.40, -14, -1645, -36.05]
    for item in valores:
        print(locale.currency(item, grouping=True, symbol='R$'))
    

if __name__ == '__main__':
    main()

from cpf_cnpj import Cpf, Cnpj
from telefone import Telefone
from mail import Email
from cep import Cep

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
    

if __name__ == '__main__':
    main()

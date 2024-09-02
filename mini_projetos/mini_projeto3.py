'''
- Desenvolva uma função que gera senhas aleatórias seguras, atendendo aos critérios: mínimo de 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais.
- Implemente uma função que receba uma senha do usuário e verifique se ela atende aos critérios de segurança mencionados. Para cada senha que não atender aos critérios, sugerir uma senha nova.
- Crie um programa que criptografa uma lista de senhas utilizando uma cifra de substituição (similar à cifra de Cesar) considerando todos os caracteres imprimíveis da tabela ASCII e armazene o resultado. Inclua uma função para descriptografar as senhas quando necessário.
'''

import string
import secrets

def gerar_senha():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(8))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            return password
        
senha_segura = gerar_senha()
print(f"Um exemplo de uma senha segura é {senha_segura}")

def verificar_senha_segura(senha):
    if (len(senha) >= 8 and
        any(c.islower() for c in senha) and
        any(c.isupper() for c in senha) and
        any(c.isdigit() for c in senha) and
        any(c in string.punctuation for c in senha)):
        print("A senha fornecida é segura")
    else:
        nova_senha = gerar_senha()
        print(f"A senha fornecida não é segura. Um exemplo de senha segura é: {nova_senha}")

senha_fornecida = input("Digite uma senha: ")
verificar_senha_segura(senha_fornecida)

def criptografar_senha(senha, chave):
    caracteres = string.printable
    tabela_traducao = str.maketrans(caracteres, caracteres[chave:] + caracteres[:chave])
    return senha.translate(tabela_traducao)

def descriptografar_senha(senha_criptografada, chave):
    caracteres = string.printable
    tabela_traducao = str.maketrans(caracteres[chave:] + caracteres[:chave], caracteres)
    return senha_criptografada.translate(tabela_traducao)

def criptografar_lista_senhas(lista_senhas, chave):
    return [criptografar_senha(senha, chave) for senha in lista_senhas]

def descriptografar_lista_senhas(lista_senhas_criptografadas, chave):
    return [descriptografar_senha(senha, chave) for senha in lista_senhas_criptografadas]

lista_senhas = ["Lara", "ABC@123", "Oie#9873"]
print(f"Lista original de senhas: {lista_senhas}")

chave = 4

lista_senhas_criptografadas = criptografar_lista_senhas(lista_senhas, chave)
print(f"Lista de senhas criptografadas: {lista_senhas_criptografadas}")

lista_senhas_descriptografadas = descriptografar_lista_senhas(lista_senhas_criptografadas, chave)
print(f"Lista de senhas descriptografadas: {lista_senhas_descriptografadas}")

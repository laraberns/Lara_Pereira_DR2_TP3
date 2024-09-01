'''
- Crie um programa com funções em Python para solicitar ao usuário que insira os dados listados abaixo e valide os seguintes campos de cadastro com as seguintes regras:
    -- CPF: verifique se o CPF possui 11 dígitos e formate-o no padrão "xxx.xxx.xxx-xx".
    -- E-mail: verifique se o e-mail possui um formato válido (com "@" e um domínio válido) e normalize-o para minúsculas. Caracteres alfanuméricos + ‘@’ + Caracteres alfanuméricos + ‘.’ + Caracteres alfabéticos
    -- Telefone: remova caracteres não numéricos e converta o número de telefone para um número inteiro e em uma string formatada como (XX) XXXXX-XXXX ou (XX) XXXX-XXXX e exibindo o inteiro e a string formatada na tela.
'''

def validar_cpf(cpf):
    if len(cpf) != 11:
        raise ValueError("Erro com o CPF inserido: O CPF deve digitado deve possuir 11 dígitos")
    
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    
    return cpf_formatado
    
def validar_email(email):
    if email.count('@') != 1:
        raise ValueError("Erro com o e-mail digitado: Ele não possui o formato válido")
    
    usuario, dominio = email.split('@')

    dominios_validos = ["gmail.com", "outlook.com"]

    if dominio not in dominios_validos:
        raise ValueError("Erro com o e-mail digitado: Ele não possui o domínio válido")
    
    return usuario.lower() + '@' + dominio.lower()

def validar_telefone(telefone):

    telefone_inteiro = ''
    telefone_formatado = ''

    for caractere in telefone:
        if caractere.isdigit():
            telefone_inteiro += caractere
    
    if len(telefone_inteiro) != 11 and len(telefone_inteiro) != 10:
        raise ValueError("Erro com o telefone digitado: Ele deve possuir 10 ou 11 dígitos")
    
    if len(telefone_inteiro) == 10:
        telefone_formatado = f"({telefone_inteiro[:2]}) {telefone_inteiro[2:7]}-{telefone_inteiro[7:10]}"
    elif len(telefone_inteiro) == 11:
        telefone_formatado = f"({telefone_inteiro[:2]}) {telefone_inteiro[2:7]}-{telefone_inteiro[7:11]}"

    return int(telefone_inteiro), telefone_formatado

try:
    cpf = input("Digite um número de CPF sem caracteres especiais. Ex: 08776598732 : ")
    validar_cpf(cpf)
    email = input("Digite um e-mail. Só é aceito gmail ou outlook. Ex: larapereira@outlook.com :")
    validar_email(email)
    telefone = input("Digite um número de telefone. Ex: (48) 98765-5432: ")
    telefone_inteiro, telefone_formatado = validar_telefone(telefone)
    print(f"Telefone inteiro: {telefone_inteiro}")
    print(f"Telefone formatado: {telefone_formatado}")
    
    print("Dados salvos com sucesso!")
except ValueError as error:
    print(f"Erro {error}.")

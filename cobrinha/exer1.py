# Calcular o resultado de uma expressão matemática básica fornecida como string pelo usuário, ignorando espaços, permitindo apenas caracteres numéricos e os operadores +, -, * e /.

string_numerica = input("Digite uma operação numérica. Ex: 2 + 3 * 4: ")

def verificar_expressao(exp):
    caracteres_permitidos = "0123456789/+-* "
    texto_limpo = ""
    
    for caractere in exp:
        if caractere in caracteres_permitidos:
            texto_limpo += caractere
    
    return texto_limpo

expressao_limpa = verificar_expressao(string_numerica)

if expressao_limpa == string_numerica:
    resultado = eval(expressao_limpa)
    print("O resultado da expressão é:", resultado)
else:
    print("A expressão contém caracteres inválidos.")

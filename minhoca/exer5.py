# Calcular a soma dos dígitos em uma string numérica fornecida pelo usuário, verificando se todos os caracteres são de fato numéricos.

string_numerica = input("Digite uma string numérica: ")

string_numerica_separada = []
numeros_adicionados = 0

if string_numerica.isdigit():
    for numero in string_numerica:
        string_numerica_separada.append(int(numero))

    for numero in string_numerica_separada:
        numeros_adicionados += numero

    print("O total adicionado é ", numeros_adicionados)
else:
      print("A entrada contém caracteres não numéricos.")


# Desenvolva um programa que solicite ao usuário uma frase e imprima o número de caracteres, de palavras e de espaços em branco nesta frase.

frase = input("Digite uma frase: ")

numero_caracteres = len(frase)
numero_palavras = len(frase.split())
numero_espaco_branco = frase.count(' ')

print("O número de caracteres é ", numero_caracteres)
print("O número de palavras é ", numero_palavras)
print("O número de espaços em branco é ", numero_espaco_branco)
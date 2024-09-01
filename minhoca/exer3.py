# Escreva uma função que receba um texto e retorne a palavra mais longa presente nele, desconsiderando pontuação.

texto_exemplo = "Eu gosto de cachorro. Lara gosta de televisão."

def remover_pontuacao(texto):
    pontuacao = ".,;:!?()[]{}<>-\"'\\/"
    texto_limpo = ""
    
    for caractere in texto:
        if caractere not in pontuacao:
            texto_limpo += caractere
    
    return texto_limpo

texto_sem_pontuacao = remover_pontuacao(texto_exemplo)

palavras = texto_sem_pontuacao.split()

maior_palavra = max(palavras, key=len)

print("A palavra mais longa é:", maior_palavra)
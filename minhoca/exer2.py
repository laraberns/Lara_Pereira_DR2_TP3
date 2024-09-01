# Crie um script em Python que substitua todas as ocorrências de uma palavra específica em uma frase por outra palavra fornecida pelo usuário. Utilize um texto de exemplo de sua preferência e escolha a palavra a ser substituída, mas a lógica precisa funcionar para outros casos.

texto_exemplo = "Eu gosto de comida e além de comida também gosto de televisão."
palavra_escolhida = input("Digite uma palavra: ")
palavra_antiga = "comida"

novo_texto = texto_exemplo.replace(palavra_antiga, palavra_escolhida)

print(f"O texto antigo era: '{texto_exemplo}' e o texto novo é '{novo_texto}'")
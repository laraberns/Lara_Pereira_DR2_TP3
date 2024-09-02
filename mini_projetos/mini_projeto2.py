'''
- Implemente um programa em Python que receba uma lista de transações, onde cada transação é representada por uma string no formato "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Total". O programa deve calcular e exibir o valor total das vendas para cada produto.
-- Crie uma função que receba a lista de transações e retorne o produto mais vendido (baseado na quantidade) e o produto que gerou a maior receita total.
-- Escreva um script que converta os valores totais de vendas para uma nova moeda, dado um fator de conversão fornecido pelo usuário. Exiba os valores convertidos no formato monetário adequado.
'''

lista_transacoes = [
    "001, Teclado Mecânico, 1, 120.00",
    "002, Mouse Gamer, 3, 85.50",
    "003, Monitor Escritório, 2, 350.00"
]

def valor_total_vendas_produto(lista_vendas):
    for produto in lista_vendas:
        partes = produto.split(', ')
        venda_total_produto = int(partes[2]) * float(partes[3])
        print(f"O valor total de vendas do produto {partes[1]} foi de R$ {venda_total_produto:.2f}.")

def mais_vendido_e_receita(lista_vendas):
    produto_mais_vendido = None
    maior_quantidade = 0
    produto_maior_receita = None
    maior_receita = 0.0

    for produto in lista_vendas:
        partes = produto.split(', ')
        quantidade = int(partes[2])
        receita = quantidade * float(partes[3])

        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            produto_mais_vendido = partes[1]
        
        if receita > maior_receita:
            maior_receita = receita
            produto_maior_receita = partes[1]

    return produto_mais_vendido, produto_maior_receita

def conversao_vendas_moeda(lista_vendas, fator_conversao):
    for produto in lista_vendas:
        partes = produto.split(', ')
        venda_total_produto = int(partes[2]) * float(partes[3])
        valor_total_produto_convertido = venda_total_produto / fator_conversao
        print(f"O valor total de vendas do produto {partes[1]} em nova moeda é: {valor_total_produto_convertido:.2f}.")

valor_total_vendas_produto(lista_transacoes)

produto_mais_vendido, produto_maior_receita = mais_vendido_e_receita(lista_transacoes)
print("O produto mais vendido por quantidade foi:", produto_mais_vendido)
print("O produto com maior receita foi:", produto_maior_receita)

fator_conversao = float(input("Digite o fator de conversão para a nova moeda: "))

conversao_vendas_moeda(lista_transacoes, fator_conversao)

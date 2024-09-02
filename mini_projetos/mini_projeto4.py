'''
- Desenvolva um programa que receba o texto completo de um contrato e extraia todas as cláusulas que mencionem valores monetários. Os valores devem ser identificados e exibidos em uma lista separada.
- Implemente uma função que, dada uma lista de termos legais, verifique quantas vezes cada termo aparece no contrato e exiba as ocorrências em ordem decrescente de frequência.  
'''

import re

contrato = """
CONTRATO DE PRESTAÇÃO DE SERVIÇOS

CLÁUSULA 1 - OBJETO DO CONTRATO

1.1. O presente contrato tem como objeto a prestação dos seguintes serviços pela CONTRATADA à CONTRATANTE:
   - Consultoria em marketing digital.
   - Desenvolvimento e manutenção de website.

CLÁUSULA 2 - VALOR E FORMA DE PAGAMENTO

2.1. O valor total do contrato é de R$ 10.000,00 (dez mil reais), que será pago da seguinte forma:
   - R$ 4.000,00 (quatro mil reais) como pagamento inicial, a ser pago na assinatura deste contrato.
   - R$ 3.000,00 (três mil reais) após 30 dias da assinatura.
   - R$ 3.000,00 (três mil reais) após 60 dias da assinatura.

CLÁUSULA 3 - PRAZO DE EXECUÇÃO

3.1. O prazo para a conclusão dos serviços é de 90 dias, contados a partir da assinatura deste contrato.
"""

def identificar_valores_monetarios(texto):
    padrao = r'\bR\$ \d{1,3}(?:\.\d{3})*,\d{2}\b'
    return re.findall(padrao, texto)

lista_valores_monetarios = identificar_valores_monetarios(contrato)
print("Valores monetários encontrados:", lista_valores_monetarios)

termos_legais = [
    "CONTRATO",
    "PRESTAÇÃO DE SERVIÇOS",
    "CONTRATANTE",
    "CONTRATADA",
    "OBJETO DO CONTRATO",
    "VALOR",
    "FORMA DE PAGAMENTO",
    "PRAZO DE EXECUÇÃO",
    "OBRIGAÇÕES DAS PARTES"
]

def identificar_termos_legais(termos_legais, contrato):
    padrao = r'\b(?:' + '|'.join(map(re.escape, termos_legais)) + r')\b'
    encontradas = re.findall(padrao, contrato, re.IGNORECASE)
    
    contagem = {termo: encontradas.count(termo) for termo in termos_legais}
    contagem_ordenada = dict(sorted(contagem.items(), key=lambda item: item[1], reverse=True))
    
    print("Frequência de termos legais:")
    for termo, freq in contagem_ordenada.items():
        print(f"{termo}: {freq}")

identificar_termos_legais(termos_legais, contrato)

# Exercícios de Performance em Python

Este projeto contém uma série de exercícios de performance para praticar e testar seus conhecimentos em Python. Cada exercício é projetado para abordar conceitos fundamentais da linguagem e ajudá-lo a aprimorar suas habilidades de programação.

## Exercícios

### Parte 1: Nível Minhoca

1. **Formatar Nome Completo**
   - Crie um programa que solicite um nome completo ao usuário e formate-o de forma que todas as palavras comecem com letra maiúscula e o restante seja minúsculo e exiba-o na tela.

2. **Substituir Palavra em uma Frase**
   - Crie um script em Python que substitua todas as ocorrências de uma palavra específica em uma frase por outra palavra fornecida pelo usuário. Utilize um texto de exemplo de sua preferência e escolha a palavra a ser substituída, mas a lógica precisa funcionar para outros casos.

3. **Encontrar a Palavra Mais Longa**
   - Escreva uma função que receba um texto e retorne a palavra mais longa presente nele, desconsiderando pontuação.

4. **Contar Caracteres, Palavras e Espaços**
   - Desenvolva um programa que solicite ao usuário uma frase e imprima o número de caracteres, de palavras e de espaços em branco nesta frase.

5. **Soma dos Dígitos**
   - Calcule a soma dos dígitos em uma string numérica fornecida pelo usuário, verificando se todos os caracteres são de fato numéricos.
   - Exemplo: “123” Resultado: 1+2+3 = 6

### Parte 2: Nível Cobrinha

1. **Calcular Expressão Matemática**
   - Calcule o resultado de uma expressão matemática básica fornecida como string pelo usuário, ignorando espaços, permitindo apenas caracteres numéricos e os operadores +, -, * e /.
   - Exemplo: '2 + 3 * 4' Resultado: 14.

2. **Formatar Data**
   - Implemente uma função que receba uma string representando uma data no formato "dd/mm/aaaa" e retorne a data em um formato textual, por exemplo, "25/12/2024" -> "Vinte e cinco de dezembro de dois mil e vinte e quatro".

### Parte 3: Mini Projetos Nível PYTHON

1. **Mini Projeto 1: Validação e Formatação de Dados em um Sistema de Cadastro**
   - Crie um programa com funções em Python para solicitar ao usuário que insira os dados listados abaixo e valide os seguintes campos de cadastro com as seguintes regras:
     - **CPF**: verifique se o CPF possui 11 dígitos e formate-o no padrão "xxx.xxx.xxx-xx".
     - **E-mail**: verifique se o e-mail possui um formato válido (com "@" e um domínio válido) e normalize-o para minúsculas.
     - **Telefone**: remova caracteres não numéricos e converta o número de telefone para um número inteiro e uma string formatada como (XX) XXXXX-XXXX ou (XX) XXXX-XXXX e exiba ambos na tela.

2. **Mini Projeto 2: Análise de Dados de Vendas**
   - Implemente um programa em Python que receba uma lista de transações no formato "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Total". O programa deve calcular e exibir o valor total das vendas para cada produto.
   - Crie uma função que retorne o produto mais vendido e o produto que gerou a maior receita total.
   - Converta os valores totais de vendas para uma nova moeda, dado um fator de conversão fornecido pelo usuário, e exiba os valores convertidos no formato monetário adequado.

3. **Mini Projeto 3: Gerenciamento de Senhas**
   - Desenvolva uma função que gera senhas aleatórias seguras, atendendo aos critérios: mínimo de 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais.
   - Implemente uma função que receba uma senha do usuário e verifique se ela atende aos critérios de segurança mencionados. Para cada senha que não atender aos critérios, sugira uma nova senha.
   - Crie um programa que criptografa uma lista de senhas utilizando uma cifra de substituição (similar à cifra de Cesar) e armazene o resultado. Inclua uma função para descriptografar as senhas quando necessário.

4. **Mini Projeto 4: Processamento de Textos Jurídicos**
   - Desenvolva um programa que receba o texto completo de um contrato e extraia todas as cláusulas que mencionem valores monetários. Exiba os valores em uma lista separada.
   - Implemente uma função que, dada uma lista de termos legais, verifique quantas vezes cada termo aparece no contrato e exiba as ocorrências em ordem decrescente de frequência.

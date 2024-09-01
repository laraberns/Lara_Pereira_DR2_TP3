
# Implemente uma função que receba uma string representando uma data no formato "dd/mm/aaaa" e retorne a data em um formato textual, por exemplo, "25/12/2024" -> "Vinte e cinco de dezembro de dois mil e vinte e quatro".

from num2words import num2words

def data_para_extenso(data):
    
    dias = [
        "primeiro", "dois", "três", "quatro", "cinco", "seis",
        "sete", "oito", "nove", "dez", "onze", "doze",
        "treze", "quatorze", "quinze", "dezesseis", "dezessete",
        "dezoito", "dezenove", "vinte", "vinte e um", "vinte e dois",
        "vinte e três", "vinte e quatro", "vinte e cinco", "vinte e seis",
        "vinte e sete", "vinte e oito", "vinte e nove", "trinta", "trinta e um"
    ]
    
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    
    try:
        dia, mes, ano = data.split('/')
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        
        if dia < 1 or dia > 31:
            raise ValueError("Dia fora do intervalo válido (1 a 31).")
        if mes < 1 or mes > 12:
            raise ValueError("Mês fora do intervalo válido (1 a 12).")
        
        dia_extenso = dias[dia - 1]
        mes_extenso = meses[mes - 1]
        
        ano_extenso = num2words(ano, lang='pt_BR')
        
        return f"{dia_extenso} de {mes_extenso} de {ano_extenso}"
    
    except ValueError as e:
        raise ValueError(f"Erro com a data inserida: {e}")

data = input("Digite uma data no formato dd/mm/aaaa. Exemplo: 25/12/2024: ")

try:
    resultado = data_para_extenso(data)
    print(f"A data digitada foi: {resultado}.")
except ValueError as error:
    print(f"Erro com a data inserida. {error}.")

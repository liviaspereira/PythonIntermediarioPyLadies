'''Faça uma função chamada idadeAtual que receba o parâmetro dataDeNascimento com o seguinte 
formato “dd/mm/aaaa”, e que retorne a idade atual de acordo com o dia de hoje (28/07/2020)'''

def idadeAtual (dataDeNascimento):
    dia, mes, ano = map(int, dataDeNascimento.split('/'))
    if mes > 7:
        if dia > 28:
            return 2020 - ano - 1
        else:
            return 2020 - ano 
    else:
        return 2020 - ano

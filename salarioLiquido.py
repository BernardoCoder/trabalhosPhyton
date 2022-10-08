imp_renda = 0.11
inss = 0.08
sindicato = 0.05


sal_horas = float(input('Quanto você ganha por hora? '))
hor_trab_mes = int(input('Quantas horas você trabalhou no mês? '))
sal_bruto = sal_horas * hor_trab_mes
d_imp_renda = sal_bruto * imp_renda
d_inss = sal_bruto * inss
d_sindicato = sal_bruto * sindicato
sal_liquido = sal_bruto - d_imp_renda - d_inss - d_sindicato




print('Seu salário Bruto é: ', sal_bruto)
print('Seu salário Liquido é: ', sal_liquido)
print('Você pagou ao INSS um total de:', d_inss)
print('Você pagou de Imposto de renda um total de: ', d_imp_renda)
print('Você pagou ao Sindicato um total de: ', d_sindicato)
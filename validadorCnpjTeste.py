'''
Esse modulo é parte de um projeto de validador de cnpj, feito em um curso na plataforma 
Udemy, esse modulo funciona em conjunto com um gerador de cnpj, assim posso estar gerando 
diversos cnpjs ao mesmo tempo
'''
from validador_de_cnpj import validar
from gerador_cnpj import format_cnpj
for i in range(100):
    validar(format_cnpj())
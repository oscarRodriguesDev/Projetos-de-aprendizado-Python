# -*- coding: utf-8 -*-
'''
Este modulo recebe o cnpj para que o mesmo possa ser validado
'''

import re

# função que remove os caracteres especiais do cnpj
def removeCht(cnpj):
    return re.sub(r'[^0-9]','',cnpj)


#função que analisa o primeiro digito do cnpj
def firstdigit(fatia_cnpj):
    cta =  [5,4,3,2,9,8,7,6,5,4,3,2] 
    cnpj =[x*int(y) for x,y in zip(cta,fatia_cnpj)]
    dig = 11-(sum(cnpj,0)%11)
    if dig>=10:
        dig= 0
    cnpj_x =  fatia_cnpj+str(dig)
    return cnpj_x
    
    

#função que valida o segundo digito do cnpj
def secondDig(fatia_cnpj):
    cta =  [6,5,4,3,2,9,8,7,6,5,4,3,2] 
    cnpj =[x*int(y) for x,y in zip(cta,fatia_cnpj)]
    dig = 11-(sum(cnpj,0)%11)
    if dig>=10:
        dig= 0
    cnpj_x =  fatia_cnpj+str(dig)
    return cnpj_x

#função que efetivamente valida o cnpj, resposavel por chamar as outras funções
def validar(cnpj):
    #primeiro digito
    a =removeCht(cnpj)
    b =firstdigit(a[:12])
    cnpjy =secondDig(a[:13])
    if a==cnpjy:
        print(f'O cnpj {cnpj} é válido!')
    else:
        print(f'O cnpj {cnpj} é inválido! Verifique novamente')
    
    



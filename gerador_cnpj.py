# -*- coding: utf-8 -*-
"""
nesse modulo estamos gerando o cnpj para que o mesmo possa ser testado pelo
modulo validador de cnpj
"""
import random

#função para gerar os numeros do cnpj 
def cnpj_init():
    numero = str(random.randrange(999999999999))
    lista =  [int(x) for x in numero]
    return lista

#função que gera o primeiro digito do cnpj
def gerard1(lista):
    cta = [5,4,3,2,9,8,7,6,5,4,3,2]
    c =  [x*y for x,y in zip(cta,lista)]
    digx =  11-(sum(c,0)%11)
    if digx>=10:
        digx= 0
    
    lista.append(digx)
    return lista

#função que gera o segundo digito do cnpj
def gerard2(lista):
    cta = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    c =  [x*y for x,y in zip(cta,lista)]
    digx =  11-(sum(c,0)%11)
    if digx>=10:
        digx= 0
    
    lista.append(digx)
    return lista
#função que reune todos os numeros gerados formando o todos os digitos do cnpj
def num_cnpj():
    c =  cnpj_init()
    d = gerard1(c)  
    a = gerard2(d)
    return a

#função que formata o cnpj em formato aceitavel pela receita federal
#função a ser chamada para gerar o cnpj    
def format_cnpj():
    cnpj=num_cnpj() 
    lista = []
    '04.252.011/0001-10'
    for i,e in  enumerate(cnpj):
        lista.append(str(e))
        if i==1:
            lista.append('.')
        if i==4:
            lista.append('.')
        if i==7:
            lista.append('/')
        if i==11:
            lista.append('-')
    cnpj =str.join('',lista)
    print(cnpj)
    return cnpj
    
#forma como podemos gerar os cnpjs  
if __name__== '__main__':    
    format_cnpj()
    
 



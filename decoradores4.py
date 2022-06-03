# -*- coding: utf-8 -*-
 
'''
nesse modulo vamos criar uma função decoradora que cria logs para qualquer função 
executada

'''
from time import sleep,time
def identificador(função):
    def geraLog(*args,**kwargs):
        #como vamos gerar os logs?
        with open('log.txt','a+') as logs:
            logs.write(f'\t•função {função.__name__} foi executada com sucesso\n')
            logs.write(f'\t•a função {função.__name__} usou os paramentros{args}\n ')
        
        função(*args,**kwargs)
    return geraLog

#vamos criar agora a função que será decorada, nesse caso uma função de soma:
@identificador
def soma(a=0,b=0):
    print(a+b)
    
#vamos criar uma função para cada operação matematica
@identificador
def subtrair(a = 0,b = 0):
    print(a-b)
@identificador  
def multiplica(a=0,b=0):
    print(a * b)
@identificador   
def divide( a=0, b=1):
    if not b ==0:
       print( a/b)
    else:
        print('impossivel dividir por zero')
        
#vamos agora executar cada uma delas
soma(3,5)
subtrair(10,3)
multiplica(5, 5)
divide(5, 5)
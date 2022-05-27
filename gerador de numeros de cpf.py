# -*- coding: utf-8 -*-
"""
Este programa gera numeros validos aleatórios de CPFs, pode ser usado em conjunto com o validador de 
CPFs para fins de teste.
obs: o numero é matematicamente válido, mas não necessariamente valido para o sistema governamental
"""
import random

#precisamos capturar o cpf, nesse caso vamos usar input
cpf =  random.randrange(99999999999)
cpf = str(cpf)

#essa verificação sera retiranda posteriormente 
if(not len(cpf)==11):
    print('o cpf é invalido, o numero de cpf tem 11 digitos!')
else:
#preciso isolar os 9 digitos
    digitos =  cpf[0:9]
    ver1 = cpf[9]
    ver2 = cpf[10]
    soma = 0
    soma2 = 0

    #iterei os 9 digitos agora tem que multiplica-los por multiplicadores decrescendo de 10 in 10
    for i, mult in enumerate(range(10, 1, -1)):
        r = int(cpf[i])*mult
        soma += r
   
    n1 = 11-(soma % 11)
  
    menor_que_nove = n1<=9
    d1 =  str(n1) if menor_que_nove else '0'
    
#agora vamos avaliar o segundo digito verificador
for i, mult in enumerate(range(11, 1, -1)):
    r = int(cpf[i])*mult
    soma2 += r
    n1 = 11-(soma2 % 11)
    menor_que_nove = n1<=9
    d2 =  str(n1) if menor_que_nove else '0'

#verificação final
cpfVerificado=  digitos+d1+d2
validado =  cpfVerificado==cpf
msg ='Cpf Validado com sucesso' if validado else 'Este numero de cpf é invalido'
print(cpf,msg,cpfVerificado)
        
            
       
    
        
       
         
            
  
    

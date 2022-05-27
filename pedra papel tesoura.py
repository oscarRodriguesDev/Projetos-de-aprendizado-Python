# -*- coding: utf-8 -*-
"""
classico joguinho pedra papel tesoura

@author: oskha
"""

import random,os
opção = 0
'''
Esta função servirá para apresentação da mensagem de erro caso  o
usuario digite um comando errado, utilizado para envio de msgs
'''
def msg():
    return'opções:\n SAIR- "sair" 1-PEDRA 2-PAPEL 3-TESOURA' 
    
#os.system('cls') #esta opção será usada apenas quando for executado diretamente no terminal
while not opção=='sair':
   # print('#'*29)   
    opção = input('digite sua opção ')
    listoptions = ['1','2','3','sair'.upper()] #lista com todas as opções possiveis para o usuario
        
    maq = str(random.randrange(1, 3))
    if opção=='sair':
        break
    elif not opção in listoptions:
        print(f'A opção {opção} não é valida tente {msg()} ')
        continue
    else:
        if not opção==maq:
            print(f'COMP escolheu {maq} e você escolheu {opção} que pena você perdeu!')
 
        else:
            print(f'COMP escolheu {maq} e você escolheu {opção} Parabens você ganhou!')

        
  

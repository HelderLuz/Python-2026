# 4. Crie um programa que utilize o módulo time para esperar 5 segundos antes de exibir uma mensagem na tela.

import time

for i in range(5,0,-1):
    print(f'{i} segundos')
    time.sleep(1)
print('Mensagem após 5 segundos')
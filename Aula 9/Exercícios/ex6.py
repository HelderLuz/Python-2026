# 6. Crie um programa que leia um caractere e informe se ele é uma vogal ou uma consoante. (Desconsidere diferença de maiúscula e minúscula)

caractere = input('Digite um caractere: ')

if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
    print('É uma vogal!')
else:
    print('É uma consoante!')
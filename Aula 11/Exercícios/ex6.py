# 6. Escreva um programa que simula um sistema de login. O usuário tem até 3 tentativas para acertar a senha correta. Se errar 3 vezes, o acesso é negado.

senha_correta = "swordfish"
tentativas = 3
senha = ''

while tentativas > 0:
    senha = input('Digite a senha: ')

    if senha == senha_correta:
        print('Senha correta! \nAcesso permitido!')
        break

    tentativas -= 1
    print('Senha incorreta!')
    print(f'Número de tentativas restantes: {tentativas}')

if tentativas == 0:
    print('Acesso negado!!!')
# 6. Escreva um programa que simula um sistema de login. O usuário tem até 3 tentativas para acertar a senha correta. Se errar 3 vezes, o acesso é negado.

senha_correta = "swordfish"
tentativas_senha = 3
senha = ''
tentativas_login = 3
login_correto = 'helderjfl'
login = ''

while tentativas_login > 0:
    login = input('Digite o login: ')

    if login == login_correto:
        print('Login correto!')
        break

    tentativas_login -= 1
    print(f'Login incorreto \n{tentativas_login} tentativas restantes.')

while login == login_correto and tentativas_senha > 0:
    senha = input('Digite a senha: ')

    if senha == senha_correta:
        print('Senha correta! \nAcesso permitido!')
        break

    tentativas_senha -= 1
    print('Senha incorreta!')
    print(f'Número de tentativas restantes: {tentativas_senha}')

if tentativas_senha == 0:
    print('Acesso negado!!!')
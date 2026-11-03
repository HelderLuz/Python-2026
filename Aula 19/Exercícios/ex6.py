# 6. Crie um dicionário para armazenar informações sobre departamentos de uma empresa. Cada chave será o nome do departamento, e o valor será outro dicionário com pares "nome_funcionario": salario.
# - Adicione pelo menos 2 departamentos e 3 funcionários em cada um.
# - Calcule a soma dos salários de todos os funcionários.
# - Liste o nome do departamento com a média salarial mais alta.
empresa = {
    'rh': {
        'joão': 2100,
        'maria': 3100,
        'josé': 3200
    },
    'marketing': {
        'paulo': 3500,
        'ana': 4000,
        'jéssica': 6000
    }
}

maior_salario = {'departamento': '', 'media_salarial': 0}
total_salarios = 0
for departamento, funcionarios in empresa.items():
    total_departamento = 0
    for salario in funcionarios.values():
        total_departamento += salario
    media_salarial = total_departamento / len(funcionarios.values())

    if maior_salario['media_salarial'] < media_salarial:
        maior_salario['departamento'] = departamento
        maior_salario['media_salarial'] = media_salarial
    total_salarios += total_departamento

print(f'Soma dos salários dos funcionários é R${total_salarios:.2f}')
print('\nMaior média salarial')
print(f'Departamento: {maior_salario['departamento']} \nMédia salárial: {maior_salario['media_salarial']:.2f}')

nota = int(input('Digite a nota: '))

if nota >= 60:  # Primeiro nível
    print("Aprovado")
    
    if nota >= 90:  # Segundo nível
        print("Excelente!")
    elif nota >= 75:  # Segundo nível
        print("Bom desempenho.")
    else: # Segundo nível
        print("Pode melhorar.")
else: # Primeiro nível
    print("Reprovado")


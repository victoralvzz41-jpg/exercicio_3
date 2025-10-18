def classificar_idade():
    """
    Solicita a idade do usuário e a classifica em categorias.
    """
    # 1. Solicita a idade do usuário
    while True:
        try:
            idade = int(input("Por favor, digite sua idade: "))
            # Garante que a idade seja um número não negativo
            if idade >= 0:
                break
            else:
                print("A idade não pode ser um número negativo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # 2. Classifica a idade usando condicionais (if/elif/else)
    
    # Criança (0-12 anos)
    if idade <= 12:
        categoria = "Criança"
        
    # Adolescente (13-17 anos)
    elif idade <= 17:
        categoria = "Adolescente"
        
    # Adulto (18-59 anos)
    elif idade <= 59:
        categoria = "Adulto"
        
    # Idoso (60 anos ou mais)
    else: # idades maiores ou iguais a 60
        categoria = "Idoso"
        
    # 3. Exibe o resultado
    print(f"\nCom {idade} anos, você se enquadra na categoria: {categoria}")

# Executa a função principal
if __name__ == "__main__":
    classificar_idade()
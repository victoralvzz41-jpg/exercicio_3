def calcular_imc():
    """
    Solicita o peso (kg) e a altura (m) do usuário, calcula o IMC
    e fornece a classificação de acordo com a tabela padrão.
    """
    # 1. Solicita e valida o Peso (em kg)
    while True:
        try:
            peso = float(input("Por favor, digite seu peso em quilogramas (ex: 70.5): "))
            if peso > 0:
                break
            else:
                print("O peso deve ser um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o peso.")

    # 2. Solicita e valida a Altura (em metros)
    while True:
        try:
            altura = float(input("Por favor, digite sua altura em metros (ex: 1.75): "))
            if altura > 0:
                break
            else:
                print("A altura deve ser um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a altura.")

    # 3. Calcula o IMC
    # Fórmula: IMC = peso / (altura * altura)
    imc = peso / (altura ** 2)

    # 4. Classificação do IMC
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        # Para os demais cenários (IMC >= 30)
        classificacao = "Obeso"

    # 5. Exibe os resultados
    print("\n--- Resultado do IMC ---")
    print(f"Peso: {peso:.2f} kg")
    print(f"Altura: {altura:.2f} m")
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")
    print("------------------------")

# Executa a função principal
if __name__ == "__main__":
    calcular_imc()
def conversor_temperatura():
    """
    Solicita a temperatura, a unidade de origem e a unidade de destino,
    e realiza a conversão entre Celsius, Fahrenheit e Kelvin.
    """
    print("--- Conversor de Temperatura ---")
    print("Unidades suportadas: C (Celsius), F (Fahrenheit), K (Kelvin)")

    # 1. Obter a unidade de origem e destino
    while True:
        unidade_origem = input("Informe a unidade de ORIGEM (C, F ou K): ").upper()
        if unidade_origem in ('C', 'F', 'K'):
            break
        print("Unidade de origem inválida. Use C, F ou K.")

    while True:
        unidade_destino = input("Informe a unidade de DESTINO (C, F ou K): ").upper()
        if unidade_destino in ('C', 'F', 'K'):
            break
        print("Unidade de destino inválida. Use C, F ou K.")

    # Se as unidades forem as mesmas, não há conversão a ser feita
    if unidade_origem == unidade_destino:
        print("\nAs unidades de origem e destino são as mesmas. Nenhuma conversão necessária.")
        # O programa continua para pegar a temperatura de qualquer forma para mostrar o resultado.

    # 2. Obter a temperatura
    while True:
        try:
            temp_origem = float(input(f"Digite a temperatura em {unidade_origem}: "))
            # Garante que a temperatura não está abaixo do zero absoluto
            if unidade_origem == 'K' and temp_origem < 0:
                 print("Temperatura em Kelvin não pode ser negativa (Zero Absoluto).")
                 continue
            if unidade_origem == 'C' and temp_origem < -273.15:
                 print("Temperatura em Celsius não pode ser inferior a -273.15°C (Zero Absoluto).")
                 continue
            if unidade_origem == 'F' and temp_origem < -459.67:
                 print("Temperatura em Fahrenheit não pode ser inferior a -459.67°F (Zero Absoluto).")
                 continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # 3. Centralizar o cálculo convertendo TUDO para Celsius primeiro
    
    # Converte a temperatura de origem para Celsius (intermediário)
    if unidade_origem == 'F':
        temp_celsius = (temp_origem - 32) * 5/9
    elif unidade_origem == 'K':
        temp_celsius = temp_origem - 273.15
    else: # Já é Celsius
        temp_celsius = temp_origem
        
    # 4. Converte de Celsius (intermediário) para a unidade de destino
    
    if unidade_destino == 'F':
        temp_final = (temp_celsius * 9/5) + 32
    elif unidade_destino == 'K':
        temp_final = temp_celsius + 273.15
    else: # O destino é Celsius (C)
        temp_final = temp_celsius

    # 5. Exibe o resultado
    print("\n--- Resultado da Conversão ---")
    print(f"Temperatura Original: {temp_origem:.2f} {unidade_origem}")
    print(f"Temperatura Convertida: {temp_final:.2f} {unidade_destino}")
    print("------------------------------")

# Executa a função principal
if __name__ == "__main__":
    conversor_temperatura()
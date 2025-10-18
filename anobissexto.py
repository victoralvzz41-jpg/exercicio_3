def verificar_ano_bissexto():
    """
    Solicita um ano ao usuário e determina se ele é bissexto
    de acordo com as regras:
    - Divisível por 4
    - Exceto anos divisíveis por 100 que não são divisíveis por 400.
    """
    print("--- Verificador de Ano Bissexto ---")

    # 1. Solicita e valida o ano
    while True:
        try:
            ano = int(input("Por favor, digite um ano (ex: 2024): "))
            if ano >= 0:
                break
            else:
                print("O ano deve ser um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o ano.")

    # 2. Aplica a Lógica do Ano Bissexto
    
    # A regra pode ser expressa em uma única linha de lógica booleana:
    # Um ano é bissexto SE:
    # (É divisível por 400) OU (É divisível por 4 E NÃO é divisível por 100)
    
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        e_bissexto = True
    else:
        e_bissexto = False

    # 3. Exibe o resultado
    print(f"\n--- Resultado da Verificação ---")
    print(f"O ano {ano} é:")
    
    if e_bissexto:
        print("Bissexto.")
    else:
        print("Não é bissexto.")
    print("--------------------------------")

# Executa a função principal
if __name__ == "__main__":
    verificar_ano_bissexto()
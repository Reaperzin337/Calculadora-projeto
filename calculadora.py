import sys

print("--- Calculadora Simples em Python ---")

while True:
    try:
        # Entrada de dados
        num1 = float(input("\nOlá, digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Digite apenas números válidos.")
        continue

    print("\n--- MENU DE OPERAÇÕES ---")
    print(" [+] Soma\n [-] Subtração\n [*] Multiplicação\n [/] Divisão\n [S] Sair")
    print("---------------------------")
    
    operador = input("Escolha a operação: ").upper()

    if operador == 'S':
        print("Saindo... Até logo!")
        break
    
    # Lógica
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 == 0:
            resultado = "Erro: Divisão por zero!"
        else:
            resultado = round(num1 / num2, 2)
    else:
        resultado = "Operação Inválida"

    print(f"O resultado é : {resultado}")

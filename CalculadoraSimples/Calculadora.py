def calculadora():
    while True:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /) ou 's' para sair: ")
        if operador.lower() == 's':
            print("Saindo da calculadora...")
            break
        num2 = float(input("Digite o segundo número: "))

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: divisão por zero!")
                continue
        else:
            print("Operador inválido!")
            continue

        print("O resultado é:", resultado)
        print("-" * 30)  # linha separadora

calculadora()

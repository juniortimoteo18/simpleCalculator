

print("pt -> Esta e' uma calculadora de operacoes simples!")
print("en -> This is a simple operations calculator!")

print("Insira { pt } para portugues")
lang = input("Insert { en } for english:")
print("")

if lang == "pt":
    ver = True
    while ver:
        print("1. Subtracao( - )")
        print("2. Adicao( + )")
        print("3. Multiplicao( * )")
        print("4. Divisao( / )")
        print("")
        op = eval(input("Escolha a operacao: "))
        print("")
        if op == 1:
            valor1 = eval(input("Insira um numnero: "))
            valor2 = eval(input("Insira um numnero: "))
            resultado = valor1 - valor2
            print("")
            print("Resultado: ",resultado)
            ver2 = eval(input("Digite qualquer tecla para continuar e 0 para sair:"))
            if ver2 == 0:
                break
        elif op == 2:
            valor1 = eval(input("Insira um numnero: "))
            valor2 = eval(input("Insira um numnero: "))
            resultado = valor1 + valor2
            print("")
            print("Resultado: ",resultado)
            ver2 = eval(input("Digite qualquer tecla para continuar e 0 para sair:"))
            if ver2 == 0:
                break
        elif op == 3:
            valor1 = eval(input("Insira um numnero: "))
            valor2 = eval(input("Insira um numnero: "))
            resultado = valor1 * valor2
            print("")
            print("Resultado: ",resultado)
            ver2 = eval(input("Digite qualquer tecla para continuar e 0 para sair:"))
            if ver2 == 0:
                break
        elif op == 4:
            valor1 = eval(input("Insira um numnero: "))
            valor2 = eval(input("Insira um numnero: "))
            resultado = valor1 / valor2
            print("")
            print("Resultado: ",resultado)
            ver2 = eval(input("Digite qualquer tecla para continuar e 0 para sair:"))
            if ver2 == 0:
                break
        else:
            print("Insira uma operacao valida!")
            print("")
elif lang == "en":
    ver = True
    while ver:
        print("1. Sub( - )")
        print("2. Add( + )")
        print("3. Multiply( * )")
        print("4. Division( / )")
        print("")
        op = eval(input("Choose operation: "))
        print("")
        if op == 1:
            value1 = eval(input("Insert a number: "))
            value2 = eval(input("Insert a number: "))
            result = value1 - value2
            print("")
            print("Result: ",result)
            ver2 = eval(input("Push any key to continue and 0 to exit: "))
            if ver2 == 0:
                break
        elif op == 2:
            value1 = eval(input("Insert a number: "))
            value2 = eval(input("Insert a number: "))
            result = value1 + value2
            print("")
            print("Result: ",result)
            ver2 = eval(input("Push any key to continue and 0 to exit: "))
            if ver2 == 0:
                break
        elif op == 3:
            value1 = eval(input("Insert a number: "))
            value2 = eval(input("Insert a number: "))
            result = value1 * value2
            print("")
            print("Result: ",result)
            ver2 = eval(input("Push any key to continue and 0 to exit: "))
            if ver2 == 0:
                break
        elif op == 4:
            value1 = eval(input("Insert a number: "))
            value2 = eval(input("Insert a number: "))
            result = value1 / value2
            print("")
            print("Result: ",result)
            ver2 = eval(input("Push any key to continue and 0 to exit: "))
            if ver2 == 0:
                break
        else:
            print("Insert valid operation!")
            print("")

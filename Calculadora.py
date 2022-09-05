def menu():
    print("Calculadora simples")
    print("Que operação deseja fazer?\n+\n-\n*\n/\n**")
    escolha = input()
    if escolha != "+" and escolha != "-" and escolha != "*" and escolha != "/" and escolha != "**":
        print("Escolha inválida!!!\nSaindo....")
        quit()
    if escolha == "**":
        print("Número para ser elevado ao quadrado")
        a = int(input())
        b = a
        calculo(a, b, escolha)
    else:
        print("Digite 2 números:\n")
        a = int(input())
        b = int(input())
        calculo(a, b, escolha)

def calculo(a, b, escolha):
    if escolha == "+":
        c = a + b
        print("O resultado da soma é: ", c)
    elif escolha == "-":
        c = a - b
        print("O resultado da subtração é: ", c)
    elif escolha == "*":
        c = a * b
        print("O resultado da multiplicação é: ", c)
    elif escolha == "/":
        c = a / b
        print("O resultado da divisão é: ", c)
    elif escolha == "**":
        c = a * b
        print("O resultado do valor ao quadrado é: ", c)
    print("Deseja sair? s ou n?")
    sair = str(input())
    if sair == "s":
        quit()
    else:
        menu()

menu()
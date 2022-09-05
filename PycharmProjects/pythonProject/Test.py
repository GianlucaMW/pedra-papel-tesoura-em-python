#divide-se o peso do paciente pela sua altura elevada ao quadrado
import sys
plus = "+"
minus = "-"
mult = "*"
divide = "/"
saida = "empty"
def menu():
    print("Oque deseja calcular? \n")
    print("+")
    print("-")
    print("*")
    print("/")
    escolha = input()
    if escolha != plus and escolha != minus and escolha != mult and escolha != divide:
        print("Inválido \n Saindo...")
        exit()
    print("Digite dois números: \n")
    a = int(input())
    b = int(input())
    calcula(a, b, escolha)

def calcula(a, b, escolha):
    if escolha == plus:
        c = a + b
        print("o resultado é:", " ", c)
        print("\n deseja sair? 1(não) ou 0(sair)")
        saida = int(input())
    elif escolha == minus:
        c = a - b
        print("o resultado é:", " ", c)
        print("\n deseja sair? 1(não) ou 0(sair)")
        saida = int(input())
    elif escolha == mult:
        c = a * b
        print("o resultado é:", " ", c)
        print("\n deseja sair? 1(não) ou 0(sair)")
        saida = int(input())
    elif escolha == divide:
        c = a / b
        print("o resultado é:", " ", c)
        print("\n deseja sair? 1(não) ou 0(sair)")
        saida = int(input())
    if saida == 1:
        print("Ué")
        menu()
    elif saida == 0:
        quit()

menu()

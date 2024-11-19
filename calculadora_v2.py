saida = ''

def adicao(a, b):
    return a + b 
def subtracao(a, b):
    return a - b
def multiplicacao(a , b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    if operacao == '+':
        resultado = adicao(num1, num2)
    elif operacao == '-':
        resultado = subtracao(num1, num2)
    elif operacao == '*':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação invalida'
    return resultado

while saida.lower() != 'n':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")
    resultado = calculadora(num1, num2, operacao)
    print("Resultado da operação: ", resultado)
    saida = input("Deseja continuar executando o programa? (S/N): ")
    if saida.lower() == 'n': print("Programa encerrado.")


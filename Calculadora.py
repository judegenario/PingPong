
#calculadora simples em python

print("\Essa é sua calculadora em Python")

#funções para cálculo dos resultados

def multiplicacao(x, y)
    return x*y

def divisao(x, y)
    return x/y

def soma(x, y)
    return x+y

def subtracao(x, y)
    return x-y

print("\n Selecione a opção\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = input("\nDigite a opção de 1 a 4: ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if op == '1':
    print("\n")
    print(num1, "+" , num2, "=", soma(num1, num2))
    print("\n")

elif op == '2'
    if num2 == '0'
        print("\nNão pode dividir por 0!\n")
    else
        print("\n")
        print(num1, "-" , num2, "=", subtracao(num1, num2))
        print("\n") 

elif op == '3'
    print("\n")
    print(num1, "*" , num2, "=", mutiplicacao(num1, num2))
    print("\n") 

elif op == '4'
    print("\n")
    print(num1, "/" , num2, "=", divisao(num1, num2))
    print("\n") 

else
    print("\nOpção inválida")
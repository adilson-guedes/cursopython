# -*- coding: utf-8 -*-
"""Atividade Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TkKAlUPjjO-WcFD_W3SHo4DptUd3E2it
"""

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
print("O primeiro número escolhido foi:",num1,", e o segundo número escolhido foi:", num2)

num1_convert = float(num1)
num2_convert = float(num2)
print(type(num1_convert))
print(type(num2_convert))

print("Vamos aprender as operações?")
operacao = input("Para escolher qual operação você deseja aplicar, digite da seguinte forma: (A)Adição, (S)Subtração, (M)Multiplicação, (D)Divisão ou (R)Resto: ")

if operacao == "A" or operacao == "a":
    print("Você selecionou a Adição, e o resultado da operação é: ",num1_convert + num2_convert)
elif operacao == "S" or operacao =="s":
    print("Você selecionou a Subtração, e o resultado da operação é: ", num1_convert - num2_convert)
elif operacao == "M" or operacao =="m":
    print("Você selecionou a Multiplicação, e o resultado da operação é: ", num1_convert * num2_convert)
elif operacao == "D" or operacao =="d":
    print("Você selecionou a Divisão, e o resultado da operação é: ", num1_convert / num2_convert)
elif operacao == "R" or operacao =="r":
    print("Você selecionou o Resto, e o resultado da operação é: ", num1_convert % num2_convert)
else:
    print("Você digitou uma opção inválida, tente novamente!")
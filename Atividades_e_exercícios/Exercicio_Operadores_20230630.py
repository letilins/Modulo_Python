#exercicio 01
print("Exercício numero 1:")

num1 = int(input("Digite um numero 1: "));
num2 = int(input("Digite um numero 2: "));

soma 			= num1 + num2;
subtracao 		= num1 - num2;
multiplicacao 	= num1 * num2;
divisao 		= num1 / num2;
#resto 			= num1 % num2;
#protencia 		= num1 ** num2;
#restoDescartado = num1 //num2;

print("soma: ", soma);
print("subtração: ", subtracao);
print("multiplicação: ", multiplicacao);
print("divisão: ", divisao);
#print("resto: ", resto);
#print("protencia" , protencia);
#print("restoDescartado: ",restoDescartado);

print()

#exercicio 02
print("Exercício numero 2:")

temperatura = int(input('digite a temperatura em graus celsius: '))
if temperatura > 100:
    print("A água está fervendo!" )
else:
    print("A água não está fervendo!" )

print()

#exercicio 03
print("Exercício numero 3:")
 
num = int(input("Digite um numero inteiro: "))
if num % 2 == 0:
    print("é Par")
else:
    print("é impar")
    
print()

#exercicio 04
print("Exercício numero 4:")

senha = input("digite a senha: ")
senhacorreta = "123456"

if senha == senhacorreta:
    print("senha está correta")
else:
    print("erro!")

print()

#exercicio 05
print("Exercício numero 5:")

idade = int(input("digite sua idade: "))

if (idade >= 18) and (idade <=30):
    print("Você está entre 18 e 30 anos")
else:
    print("Não está entre 18 e 30 anos")

print()

#exercicio 06
print("Exercício numero 6:")

num1 = int(input("Digite um numero 1: "))
num2 = int(input("Digite um numero 2: "))
num3 = int(input("Digite um numero 3: "))

print()

if (num1 > 0) or (num2 > 0) or (num3 >0):
    print("menos um deles é positivo")
else:
    print("não é positivo")
    
print()
#exercicio 07
print("Exercício numero 7:")

letraVogal = input("digite uma letra: ")

if (letraVogal == 'a') or (letraVogal == 'e') or (letraVogal == 'i') or (letraVogal == 'o') or (letraVogal == 'u'):
    print("A letra é vogal")
else:
    print('A letra não é vogal')
    
print()

#exercicio 08
print("Exercício numero 8:")

num = int(input("Digite um numero inteiro: "))

if num > 0:
    print("Postivo")
elif num < 0:
    print("negativo")
else:
    print("zero")
    
print()

#exercicio 09
print("Exercício numero 9:")

num1 = int(input("Digite um numero 1: "))
num2 = int(input("Digite um numero 2: "))
num3 = int(input("Digite um numero 3: "))

if (num1 < num2) and (num2 < num3):
    print("estão em ordem crescente")
else:
    print("não estão em ordem crescente")

print()

#exercicio 10
print("Exercício numero 10:")

numero = int(input("Digite um numero 1: "))

if (numero % 3 == 0) and (numero % 5 == 0):
    print("O numero é um múltiplo de 3 e 5 ao mesmo tempo" )
else:
    print("Não é um múltiplo de 3 e 5 ")


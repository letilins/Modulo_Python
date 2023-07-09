#Exercício numero 1

print("Exercício numero 1:")
numero = 0
while numero < 10:
    numero = numero + 1
    print(numero)

print()

#Exercício numero 2

print("Exercício numero 2:")

for numero in range (1, 11):
    print(numero)

print()

#Exercício numero 3

print("Exercício numero 3:")

numero = 1
soma = 0

while numero <= 100:
    soma = numero + soma
    numero = numero + 1
    print("soma dos números de 1 a 100: ", soma)
    
print()

#Exercício numero 4

print("Exercício numero 4:")
soma = 0
numero = 1
for numero in range (1, 101):
    soma = soma + numero
    print(soma)

print()

#Exercício numero 5

print("Exercício numero 5:")

numero = 1

while numero <= 20:
    if numero % 2 == 0:  
        print(numero)   
    numero += 1       

print()

#Exercício numero 6

print("Exercício numero 6:")  

for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)

print()

#Exercício numero 7

print("Exercício numero 7:")  

palavra = input("Digite uma palavra: ")

palavra_invertida  = ""
inverta = len(palavra) - 1

while inverta >= 0:
    palavra_invertida += palavra[inverta]
    inverta -= 1
print("Palavra invertida:", palavra_invertida)

print()

#Exercício numero 8

print("Exercício numero 8:")  

palavra = input("Digite uma palavra: ")
palavra = palavra.lower()
invertido = True

for letra in range(len(palavra)):
    if palavra[letra] != palavra[-letra - 1]:
        invertido = False
    break
if invertido:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

print()

#Exercício numero 9

print("Exercício numero 9:")  

numero = 1

while numero ** 2 <= 1000:
    numero += 1
print(numero)

print()
#Exercício numero 10

print("Exercício numero 10:")  

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for letra in range(len(lista)- 1, -1, -1):
    print(lista[letra])

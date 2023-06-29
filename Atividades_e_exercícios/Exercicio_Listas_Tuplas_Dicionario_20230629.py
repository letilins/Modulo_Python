#Exercício numero 1

print("Exercício numero 1:")

frutas = ["maçã" , "banana" , "abacaxi" , "melancia" ]
print(frutas)

print()

#Exercício numero 2

print("Exercício numero 2:")

frutas = ["maçã" , "banana" , "abacaxi" , "melancia" ]
frutas.append("uva");
print("Adiciona fruta uva da lista: " , frutas)

print()

#Exercício numero 3

print("Exercício numero 3:")

frutas = ["maçã" , "banana" , "abacaxi" , "melancia" ]
frutas.remove("banana")
print("Remove fruta banana da lista: ", frutas)

print()

#Exercício numero 4

print("Exercício numero 4:")
frutas = ["maçã" , "banana" , "abacaxi" , "melancia" ]
fruta_selecionada = frutas[1]
print("Fruta selecionada: ", fruta_selecionada)

print()

#Exercício numero 5

print("Exercício numero 5:")
cores_tupla = ("vermelho" , "azul" , "verde" , "amarelo" , "roxo")
print(cores_tupla)

print()

#Exercício numero 6

print("Exercício numero 6:")
cores_tupla = ("vermelho" , "azul" , "verde" , "amarelo" , "roxo")
cor_selecionada = cores_tupla[3]
print("Cor selecionada: ", cor_selecionada)

print()

#Exercício numero 7

print("Exercício numero 7:")
#cores_tupla = ("vermelho" , "azul" , "verde" , "amarelo" , "roxo")
#cores_tupla.append("laranja")
#print(cores_tupla)
print("os elementos de Tupla não podem ser modificados porque o método append() é usado para adicionar elementos a listas")

print()

#Exercício numero 8

print("Exercício numero 8:")
aluno = {
    'nome'   : 'Leticia',
    'idade'  : 38,
    'cidade' : 'Rio de Janeiro'
}

print(aluno)

print()

#Exercício numero 9

print("Exercício numero 9:")
idade_aluno = aluno["idade"]
print("idade do aluno:" , idade_aluno)

print()

#Exercício numero 10

print("Exercício numero 10:")
aluno["gênero"] = "feminino"
print(aluno)

print()
#Exercício numero 11

print("Exercício numero 11:")
removecidadeAluno = aluno.pop("cidade")
print(removecidadeAluno)
print("Dicionário atualizado: ", aluno)

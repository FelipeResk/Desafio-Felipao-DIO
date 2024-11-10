#importações
from classes import Cat
from funcoes import typeOfCat

#Seu gato / declaração de vars
name = str(input("Qual o nome do seu gato?\n"))
age = int(input("Qual a idade dele/a (em anos)?\n"))
type = typeOfCat()

cat = Cat(name, age, type)
fur = cat.catFur()

#resposta
print(f"O gato de nome {cat.name}")
print(f"Tem {cat.age} anos")
print(f"E seu tipo por ser {cat.type} tem o pelo {fur}")
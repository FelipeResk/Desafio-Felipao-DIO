from funcoes import escolher_tipo
from classes import Heroi

print("Bem vindo a aventura final do bootcamp GFT")
nome = str(input("Me diga... Qual seu nome? \n")).capitalize()
idade = int(input("Muito bem, muito bem... E qual sua idade? \n"))
tipo = escolher_tipo()

heroi = Heroi(nome, idade, tipo)

print(f"O Herói de nome {heroi.nome}")
print(f"Com a idade de {heroi.idade}")
print(f"Do tipo {heroi.tipo}")
heroi.atacar()
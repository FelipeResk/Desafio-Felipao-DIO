from funcoes import determinar_nivel

# Declaração de variáveis
nome = input("Qual o nome do seu herói? ")
nome = nome.capitalize()
xp = int(input("Quanto XP você conseguiu? "))

# Chamada da função
nivel = determinar_nivel(xp)

# Exibição de resultado
print(f"O herói de nome {nome} está no nível {nivel}")

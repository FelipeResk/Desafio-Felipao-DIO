#importações
from funcoes import determinar_rank

#declaração de vars
totVitorias = int(input("Qual seu total de vitórias? "))
totDerrotas = int(input("Qual seu total de derrotas? "))
saldo = totVitorias - totDerrotas

rank = determinar_rank(totVitorias, totDerrotas)

print(f"Seu cartel de vitorias/derrotas é de {totVitorias}/{totDerrotas} "
    f"e seu saldo é {'positivo ' if totVitorias > totDerrotas
                     else 'negativo ' if totDerrotas > totVitorias else 'neutro '}"
                     f"de {saldo}. "
    f"\nSeu rank é {rank}.")
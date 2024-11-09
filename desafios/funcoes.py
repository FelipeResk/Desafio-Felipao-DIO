#dicionário de cores ANSI
cores = {
    "Ferro":"\033[90m", #cinza
    "Bronze":"\033[33m", #marrom
    "Prata":"\033[37m", #prata
    "Ouro":"\033[93m", #dourado
    "Platina no nariz":"\033[96m", #azul claro
    "Ascendente":"\033[35m", #roxo
    "Imortal":"\033[31m", #vermelho
    "Radiante":"\033[97m" #branco
}
reset_cor = "\033[0m" #reset da cor

def determinar_nivel(xp):
    #declaração da estrutura de decisão
    if xp < 1000:
        nivel = "Ferro"
    elif 1000 <= xp < 2000:
        nivel = "Bronze"
    elif 2000 <= xp < 5000:
        nivel = "Prata"
    elif 5000 <= xp < 7000:
        nivel = "Ouro"
    elif 7000 <= xp < 8000:
        nivel = "Platina no nariz"
    elif 8000 <= xp < 9000:
        nivel = "Ascendente"
    elif 9000 <= xp < 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"
    return f"`{cores[nivel]}{nivel}{reset_cor}"

def determinar_rank(vitorias, derrotas):
    total = vitorias - derrotas
    if total < 10:
        rank = "Ferro"
    elif 10 <= total < 20:
        rank = "Bronze"
    elif 20 <= total < 50:
        rank = "Prata"
    elif 50 <= total < 70:
        rank = "Ouro"
    elif 70 <= total < 80:
        rank = "Platina no nariz"
    elif 80 <= total < 90:
        rank = "Ascendente"
    elif 90 <= total < 100:
        rank = "Imortal"
    else:
        rank = "Radiante"
    return f"`{cores[rank]}{rank}{reset_cor}"
import copy
from jogo import verificar_vitoria, tabuleiro_cheio

def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vitoria(tabuleiro, "O"):
        return 1
    elif verificar_vitoria(tabuleiro, "X"):
        return -1
    elif tabuleiro_cheio(tabuleiro):
        return 0

    if maximizando:
        melhor_valor = -float("inf")
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == " ":
                    tabuleiro[i][j] = "O"
                    valor = minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[i][j] = " "
                    melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = float("inf")
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == " ":
                    tabuleiro[i][j] = "X"
                    valor = minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[i][j] = " "
                    melhor_valor = min(melhor_valor, valor)
        return melhor_valor

def melhor_jogada(tabuleiro):
    melhor_valor = -float("inf")
    jogada = None
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = "O"
                valor = minimax(tabuleiro, 0, False)
                tabuleiro[i][j] = " "
                if valor > melhor_valor:
                    melhor_valor = valor
                    jogada = (i, j)
    return jogada

def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tabuleiro(tab):
    for linha in tab:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(tab, jogador):
    for i in range(3):
        if all([tab[i][j] == jogador for j in range(3)]) or all([tab[j][i] == jogador for j in range(3)]):
            return True
    if all([tab[i][i] == jogador for i in range(3)]) or all([tab[i][2-i] == jogador for i in range(3)]):
        return True
    return False

def tabuleiro_cheio(tab):
    return all([celula != " " for linha in tab for celula in linha])

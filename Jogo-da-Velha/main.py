from jogo import criar_tabuleiro, imprimir_tabuleiro, verificar_vitoria, tabuleiro_cheio
from ia import melhor_jogada

def main():
    tabuleiro = criar_tabuleiro()
    jogador = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)

        if jogador == "X":
            linha = int(input("Linha (0-2): "))
            coluna = int(input("Coluna (0-2): "))
        else:
            print("IA está pensando...")
            linha, coluna = melhor_jogada(tabuleiro)

        if tabuleiro[linha][coluna] != " ":
            print("Movimento inválido. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador

        if verificar_vitoria(tabuleiro, jogador):
            imprimir_tabuleiro(tabuleiro)
            print(f"{jogador} venceu!")
            break
        elif tabuleiro_cheio(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador = "O" if jogador == "X" else "X"

if __name__ == "__main__":
    main()

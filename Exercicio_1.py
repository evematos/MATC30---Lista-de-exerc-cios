import random

def calcular_probabilidade_fuga(linhas, colunas, qtd_tuneis, labirinto, tuneis):
    from collections import defaultdict

    mapa_tuneis = {}
    for x1, y1, x2, y2 in tuneis:
        mapa_tuneis[(x1, y1)] = (x2, y2)
        mapa_tuneis[(x2, y2)] = (x1, y1)

    memoizacao = {}
    def busca_profundidade(x, y):
        if (x, y) in memoizacao:
            return memoizacao[(x, y)]
        if labirinto[x][y] == '%':
            return 1.0
        if labirinto[x][y] == '*':
            return 0.0

        labirinto[x] = labirinto[x][:y] + '#' + labirinto[x][y+1:] 
        movimentos_possiveis = 0
        soma_probabilidades = 0.0

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < linhas and 0 <= ny < colunas and labirinto[nx][ny] != '#':
                if (nx, ny) in mapa_tuneis:
                    nx, ny = mapa_tuneis[(nx, ny)]
                soma_probabilidades += busca_profundidade(nx, ny)
                movimentos_possiveis += 1

        labirinto[x] = labirinto[x][:y] + 'O' + labirinto[x][y+1:] 
        memoizacao[(x, y)] = soma_probabilidades / movimentos_possiveis if movimentos_possiveis else 0.0
        return memoizacao[(x, y)]

    for linha_idx in range(linhas):
        for coluna_idx in range(colunas):
            if labirinto[linha_idx][coluna_idx] == 'A':
                return busca_profundidade(linha_idx, coluna_idx)

    return 0.0

def criar_labirinto_randomico(linhas, colunas):
    elementos = ['O'] * 5 + ['#', '*', '%']
    labirinto_gerado = [''.join(random.choice(elementos) for _ in range(colunas)) for _ in range(linhas)]
    pos_x, pos_y = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
    linha_lista = list(labirinto_gerado[pos_x])
    linha_lista[pos_y] = 'A'
    labirinto_gerado[pos_x] = ''.join(linha_lista)
    return labirinto_gerado

def criar_tuneis_aleatorios(qtd_tuneis, linhas, colunas):
    conjunto_tuneis = set()
    while len(conjunto_tuneis) < qtd_tuneis:
        x1, y1 = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
        x2, y2 = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
        if (x1 != x2 or y1 != y2) and abs(x1 - x2) + abs(y1 - y2) > 1:
            conjunto_tuneis.add((x1, y1, x2, y2))
    return list(conjunto_tuneis)

def executar():
    linhas, colunas, qtd_tuneis = 5, 6, 2
    labirinto = criar_labirinto_randomico(linhas, colunas)
    tuneis = criar_tuneis_aleatorios(qtd_tuneis, linhas, colunas)

    print("Labirinto gerado:")
    for linha in labirinto:
        print(linha)
    print("Lista de túneis:", tuneis)

    probabilidade = calcular_probabilidade_fuga(linhas, colunas, qtd_tuneis, labirinto, tuneis)
    print(f"Chance de Alef escapar do labirinto: {probabilidade:.6f}")

if __name__ == '__main__':
    executar()
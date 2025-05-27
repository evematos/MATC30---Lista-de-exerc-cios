import random
from collections import defaultdict

def pares_similares(qtd_nos, lim_k, conexoes):
    arvore = defaultdict(list)
    for pai, filho in conexoes:
        arvore[pai].append(filho)

    contador = 0

    def busca_profundidade(no_atual, lista_ancestrais):
        nonlocal contador
        for anc in lista_ancestrais:
            if abs(anc - no_atual) <= lim_k:
                contador += 1
        for filho in arvore[no_atual]:
            busca_profundidade(filho, lista_ancestrais + [no_atual])

    raiz = set(range(1, qtd_nos + 1)) - {filho for _, filho in conexoes}
    busca_profundidade(raiz.pop(), [])

    return contador

def gerar_casos_de_teste():
    return [
        (5, 2, [(3, 2), (3, 1), (1, 4), (1, 5)]),
        (6, 3, [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)]),
        (4, 1, [(1, 2), (2, 3), (3, 4)]),
        (7, 4, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7)]),
        (3, 0, [(1, 2), (2, 3)])
    ]

def executar():
    casos = gerar_casos_de_teste()
    for numero, (qtd_nos, limite, ligações) in enumerate(casos, 1):
        print(f"Execução do Caso #{numero}")
        print(f"Nós: {qtd_nos}, Limite k: {limite}, Conexões: {ligações}")
        resultado_final = pares_similares(qtd_nos, limite, ligações)
        print(f"Pares similares encontrados: {resultado_final}\n")

if __name__ == "__main__":
    executar()

import random
from bisect import insort, bisect_left

def avisos_atividade(despesas, periodo):
    janela = sorted(despesas[:periodo])
    avisos = 0

    for idx in range(periodo, len(despesas)):
        if periodo % 2 == 1:
            med = janela[periodo // 2]
        else:
            med = (janela[periodo // 2] + janela[periodo // 2 - 1]) / 2

        if despesas[idx] >= 2 * med:
            avisos += 1

        valor_antigo = despesas[idx - periodo]
        janela.pop(bisect_left(janela, valor_antigo))
        insort(janela, despesas[idx])

    return avisos

def gerar_gastos_aleatorios(tamanho, maximo=200):
    return [random.randint(0, maximo) for _ in range(tamanho)]

def executar():
    tamanho, periodo = 10, 5
    lista_gastos = gerar_gastos_aleatorios(tamanho)

    print(f"Tamanho = {tamanho}, Período = {periodo}")
    print("Lista de gastos:", lista_gastos)

    total_avisos = avisos_atividade(lista_gastos, periodo)
    print("Total de avisos gerados:", total_avisos)

if __name__ == '__main__':
    executar()
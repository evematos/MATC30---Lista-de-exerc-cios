import random

def ordenar_insercao(vetor):
    contador_desloc = 0

    for indice_atual in range(1, len(vetor)):
        valor_atual = vetor[indice_atual]
        pos = indice_atual - 1

        while pos >= 0 and vetor[pos] > valor_atual:
            vetor[pos + 1] = vetor[pos]
            contador_desloc += 1
            pos -= 1

        vetor[pos + 1] = valor_atual
        
    return contador_desloc

def criar_vetor_aleatorio(tamanho, minimo=1, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(tamanho)]

def executar():
    vetor_entrada = criar_vetor_aleatorio(10)
    print("Vetor inicial:", vetor_entrada)
    deslocamentos = ordenar_insercao(vetor_entrada)
    print("Número total de deslocamentos:", deslocamentos)

if __name__ == '__main__':
    executar()

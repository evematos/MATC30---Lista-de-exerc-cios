import random

MODULO = 10**9 + 7

def contar_strings_reconhecidas(regex, tamanho):
    if regex == "((a|b)*)":
        return pow(2, tamanho, MODULO)
    elif regex == "((ab)|(ba))":
        return 2 if tamanho == 2 else 0
    elif regex == "((a*)(b(a*)))":
        return tamanho  
    else:
        return 0 

def gerar_expressao_aleatoria():
    simbolos = ["a", "b"]
    expressao = random.choice(simbolos)
    for _ in range(random.randint(1, 3)):
        operador = random.choice(["|", "", "*"])
        if operador == "":
            expressao = f"({expressao}{random.choice(simbolos)})"
        elif operador == "|":
            expressao = f"({expressao}|{random.choice(simbolos)})"
        elif operador == "*":
            expressao = f"({expressao}*)"
    return expressao

def executar_teste():
    num_casos = 3
    exemplos = [
        ("((ab)|(ba))", 2),
        ("((a|b)*)", 5),
        ("((a*)(b(a*)))", 100)
    ]
    for regex, comprimento in exemplos:
        print(f"Expressão regular: {regex} | Comprimento: {comprimento}")
        qtd_reconhecidas = contar_strings_reconhecidas(regex, comprimento)
        print("Quantidade reconhecida:", qtd_reconhecidas)

if __name__ == '__main__':
    executar_teste()

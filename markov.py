import random

# Treinamento
frases = [
    "o urubu voa sobre a cidade",
    "a equipe domina o jogo de vôlei",
    "o avião caiu na montanha azul",
    "eu admiro o cuidado com a saúde",
    "o urso encontrou a saída do labirinto",
    "a menina ouviu uma história incrível",
    "eu vou arrumar o jardim da casa hoje",
    "o jacaré ataca a vítima no rio turvo",
    "a roupa caiu do varal e sujou muito",
    "o aluno resolveu a equação rapidamente"
]

# Construção do modelo
def construir_modelo_markov(frases):
    modelo = {}

    for frase in frases:
        palavras = frase.split()
        for i in range(len(palavras) - a1):
            palavra_atual = palavras[i]
            proxima_palavra = palavras[i + 1]

            if palavra_atual not in modelo:
                modelo[palavra_atual] = []

            modelo[palavra_atual].append(proxima_palavra)

    print(modelo)
    return modelo

# Previsão da palavra
def prever_proxima_palavra(modelo, palavra_atual):
    if palavra_atual in modelo:
        return random.choice(modelo[palavra_atual])
    else:
        return None

# Construindo o modelo de Markov a partir do treinamento
modelo_markov = construir_modelo_markov(frases)

# Exemplo de uso
palavra_inicial = "a"
print("Palavra inicial:", palavra_inicial)

# Gerando uma frase de até 5 tokens
frase_gerada = [palavra_inicial]
for _ in range(5):
    proxima_palavra = prever_proxima_palavra(modelo_markov, frase_gerada[-1])
    if not proxima_palavra:
        break
    frase_gerada.append(proxima_palavra)

print("Frase gerada:", " ".join(frase_gerada))

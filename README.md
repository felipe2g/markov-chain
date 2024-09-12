# Gerador de Frases com Modelo de Cadeia de Markov

Este projeto implementa um gerador de frases utilizando um **Modelo de Cadeia de Markov**, que é treinado a partir de um conjunto de frases predefinidas. O modelo utiliza transições entre palavras com base na frequência de suas aparições consecutivas, permitindo prever a próxima palavra e gerar novas sequências de palavras.

## Funcionalidades

- **Treinamento**: O modelo é treinado com um conjunto de frases, criando uma estrutura que armazena as transições prováveis entre palavras.
- **Construção do Modelo**: A função `construir_modelo_markov` cria uma tabela de transições, onde cada palavra aponta para uma lista de palavras que podem segui-la.
- **Previsão de Palavras**: A função `prever_proxima_palavra` usa o modelo treinado para prever a próxima palavra com base na palavra atual.
- **Geração de Frases**: A partir de uma palavra inicial, o modelo gera novas frases escolhendo probabilisticamente a próxima palavra com base nas transições conhecidas.

## Exemplo de Uso

1. O modelo é treinado com a seguinte lista de frases:

    ```python
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
    ```

2. Construção do modelo de Markov:

    ```python
    modelo_markov = construir_modelo_markov(frases)
    ```

3. Geração de uma nova frase a partir de uma palavra inicial:

    ```python
    palavra_inicial = "a"
    frase_gerada = [palavra_inicial]
    for _ in range(5):
        proxima_palavra = prever_proxima_palavra(modelo_markov, frase_gerada[-1])
        if not proxima_palavra:
            break
        frase_gerada.append(proxima_palavra)
    
    print("Frase gerada:", " ".join(frase_gerada))
    ```

## Como Funciona

O modelo de Cadeia de Markov funciona com base em transições probabilísticas entre palavras, construindo uma tabela de estados onde cada palavra está associada a uma lista de palavras que podem segui-la. A próxima palavra é escolhida aleatoriamente da lista de palavras possíveis, com base no treinamento fornecido pelas frases.

## Referências

Este projeto é baseado no conceito de Cadeias de Markov, um modelo probabilístico usado para prever estados futuros com base em informações passadas. Para mais detalhes sobre o funcionamento de Cadeias de Markov, você pode consultar o seguinte artigo:

- **Fonte**: [Understanding Markov Chains](https://en.wikipedia.org/wiki/Markov_chain)

Inspirado por exemplos do artigo de Cadeias de Markov e implementações básicas da teoria probabilística.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

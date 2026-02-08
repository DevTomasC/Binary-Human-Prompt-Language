
## saída: Python

def busca_binaria_iterativa(array: list, alvo: int) -> int:
    """
    Realiza uma busca binária de forma iterativa em uma lista ordenada.

    Args:
        array: A lista ordenada onde a busca será realizada.
        alvo: O valor que está sendo procurado.

    Returns:
        O índice do alvo na lista, se encontrado. Caso contrário, retorna -1.
    """
    # Define o espaço de busca inicial. 'esquerda' começa no primeiro índice (0)
    # e 'direita' no último índice da lista.
    esquerda, direita = 0, len(array) - 1

    # O laço continua enquanto o espaço de busca for válido (esquerda <= direita).
    # Se 'esquerda' se tornar maior que 'direita', significa que o espaço de busca
    # se esgotou e o alvo não foi encontrado.
    while esquerda <= direita:
        # Calcula o índice do meio do espaço de busca atual.
        # Usamos (esquerda + (direita - esquerda) // 2) em vez de (esquerda + direita) // 2
        # para evitar um potencial 'overflow' em linguagens de baixo nível com
        # listas muito grandes. Em Python é mais um bom hábito de engenharia.
        meio = esquerda + (direita - esquerda) // 2

        # Compara o elemento no meio com o nosso alvo.
        if array[meio] == alvo:
            # Encontramos o alvo. Retornamos seu índice.
            return meio
        elif array[meio] < alvo:
            # Se o elemento do meio é menor que o alvo, significa que o alvo
            # só pode estar na metade direita do espaço de busca.
            # Portanto, ajustamos nosso limite da 'esquerda' para uma posição
            # depois do 'meio'.
            esquerda = meio + 1
        else:
            # Se o elemento do meio é maior que o alvo, o alvo só pode estar
            # na metade esquerda. Ajustamos nosso limite da 'direita'.
            direita = meio - 1

    # Se o laço terminar, o alvo não está na lista.
    return -1


##using Google Gemini
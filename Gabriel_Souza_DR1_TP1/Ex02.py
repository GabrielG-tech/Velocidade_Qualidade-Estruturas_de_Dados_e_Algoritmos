# Pegue um baralho de cartas: retire as 13 cartas de espadas, reserve o resto e embaralhe as cartas de espadas. Elabore um algoritmo para ordená-las por número sob as seguintes restrições

import random

cartas_espadas = list(range(1, 14))
random.shuffle(cartas_espadas)

def insertion_sort(cartas):
    # Simular a 2º mão pegando uma carta por vez e inserindo na posição correta na 1º mão
    for i in range(1, len(cartas)):
        carta_atual = cartas[i]  # A 2º mão pega a carta atual
        j = i - 1
        
        # Mover as cartas da 1º mão para frente, se forem maiores que a carta atual
        while j >= 0 and cartas[j] > carta_atual:
            cartas[j + 1] = cartas[j]  # Mover a carta para frente
            j -= 1
        
        # Inserir a carta da 2º mão na posição correta
        cartas[j + 1] = carta_atual

# Antes da ordenação
print("Cartas embaralhadas de espadas:", cartas_espadas)

# Depois da ordenação
insertion_sort(cartas_espadas)
print("Cartas ordenadas de espadas:", cartas_espadas)

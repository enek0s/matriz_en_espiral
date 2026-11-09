matriz = [
    [1, 2, 3,4,5,6,8],
    [4, 5, 6,3,4,6,7],
    [7, 8, 9,3,4,5,6],
    [4, 5, 6,3,4,6,7],
    [4, 5, 6,3,4,6,7]
]
arriba = 0
abajo = len(matriz) - 1
izquierda = 0
derecha = len(matriz[0]) - 1

resultado = []

while izquierda <= derecha and arriba <= abajo:
    # 1. Izquierda a derecha
    for col in range(izquierda, derecha + 1):
        resultado.append(matriz[arriba][col])
    arriba += 1

    # 2. Arriba a abajo
    for fila in range(arriba, abajo + 1):
        resultado.append(matriz[fila][derecha])
    derecha -= 1

    # 3. Derecha a izquierda
    if arriba <= abajo:
        for col in range(derecha, izquierda - 1, -1):
            resultado.append(matriz[abajo][col])
        abajo -= 1

    # 4. Abajo a arriba
    if izquierda <= derecha:
        for fila in range(abajo, arriba - 1, -1):
            resultado.append(matriz[fila][izquierda])
        izquierda += 1

print(resultado)

"""
Multiplicación de Matrices
Complejidad: O(n³)
"""


def multiplicar_matrices(A, B):
    """
    Multiplica dos matrices cuadradas de tamaño n x n.
    
    Args:
        A (list): Primera matriz (n x n)
        B (list): Segunda matriz (n x n)
    
    Returns:
        list: Matriz resultado de la multiplicación (n x n)
    
    Complejidad temporal: O(n³)
    Complejidad espacial: O(n²)
    """
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C


def imprimir_matriz(matriz):
    """
    Imprime una matriz de forma legible.
    
    Args:
        matriz (list): Matriz a imprimir
    """
    for fila in matriz:
        print([f"{x:3}" for x in fila])


if __name__ == "__main__":
    # Ejemplos de uso
    
    # Matrices 2x2
    A = [[1, 2], 
         [3, 4]]
    
    B = [[5, 6], 
         [7, 8]]
    
    print("Matriz A:")
    imprimir_matriz(A)
    
    print("\nMatriz B:")
    imprimir_matriz(B)
    
    resultado = multiplicar_matrices(A, B)
    print("\nA × B:")
    imprimir_matriz(resultado)
    
    # Matrices 3x3
    print("\n" + "="*30)
    A3 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    
    B3 = [[9, 8, 7],
          [6, 5, 4],
          [3, 2, 1]]
    
    print("\nMatriz A (3x3):")
    imprimir_matriz(A3)
    
    print("\nMatriz B (3x3):")
    imprimir_matriz(B3)
    
    resultado3 = multiplicar_matrices(A3, B3)
    print("\nA × B (3x3):")
    imprimir_matriz(resultado3)

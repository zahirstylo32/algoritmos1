"""
Búsqueda Binaria
Complejidad: O(log n)
Descripción: Algoritmo divide y conquista que busca en un array ORDENADO.
"""


def busqueda_binaria(arr, x):
    """
    Busca un elemento en un array ORDENADO usando divide y conquista.
    
    Args:
        arr (list): Array ORDENADO donde se realiza la búsqueda
        x: Elemento a buscar
    
    Returns:
        int: Índice del elemento si existe, -1 en caso contrario
    
    Complejidad temporal: O(log n)
    Complejidad espacial: O(1)
    
    Ventajas:
        - Muy rápida para arrays grandes
        - Mejor que búsqueda lineal
    
    Desventajas:
        - El array DEBE estar ordenado
        - No funciona en arrays desordenados
    """
    izq = 0
    der = len(arr) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        
        if arr[medio] == x:
            return medio
        elif arr[medio] < x:
            izq = medio + 1
        else:
            der = medio - 1
    
    return -1


def busqueda_binaria_recursiva(arr, x, izq=0, der=None):
    """
    Versión recursiva de la búsqueda binaria.
    
    Args:
        arr (list): Array ORDENADO
        x: Elemento a buscar
        izq (int): Índice izquierdo
        der (int): Índice derecho
    
    Returns:
        int: Índice del elemento si existe, -1 en caso contrario
    """
    if der is None:
        der = len(arr) - 1
    
    if izq > der:
        return -1
    
    medio = (izq + der) // 2
    
    if arr[medio] == x:
        return medio
    elif arr[medio] < x:
        return busqueda_binaria_recursiva(arr, x, medio + 1, der)
    else:
        return busqueda_binaria_recursiva(arr, x, izq, medio - 1)


if __name__ == "__main__":
    # Ejemplos de uso
    
    # IMPORTANTE: El array DEBE estar ordenado
    numeros = [10, 25, 30, 45, 50, 70, 80, 90]
    print("Array (ORDENADO):", numeros)
    print("="*50)
    
    # Búsqueda iterativa
    print("\n--- Búsqueda Binaria Iterativa ---")
    
    resultado = busqueda_binaria(numeros, 50)
    print(f"Buscar 50: índice {resultado}")
    
    resultado = busqueda_binaria(numeros, 25)
    print(f"Buscar 25: índice {resultado}")
    
    resultado = busqueda_binaria(numeros, 100)
    print(f"Buscar 100: índice {resultado}")
    
    # Búsqueda recursiva
    print("\n--- Búsqueda Binaria Recursiva ---")
    
    resultado = busqueda_binaria_recursiva(numeros, 70)
    print(f"Buscar 70: índice {resultado}")
    
    resultado = busqueda_binaria_recursiva(numeros, 45)
    print(f"Buscar 45: índice {resultado}")
    
    resultado = busqueda_binaria_recursiva(numeros, 15)
    print(f"Buscar 15: índice {resultado}")

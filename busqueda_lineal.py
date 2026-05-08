"""
Búsqueda Lineal
Complejidad: O(n)
Descripción: Recorre el array secuencialmente hasta encontrar el elemento.
"""


def busqueda_lineal(arr, x):
    """
    Busca un elemento en un array de forma lineal.
    
    Args:
        arr (list): Array donde se realiza la búsqueda
        x: Elemento a buscar
    
    Returns:
        int: Índice del elemento si existe, -1 en caso contrario
    
    Complejidad temporal: O(n)
    Complejidad espacial: O(1)
    
    Ventajas:
        - Simple de implementar
        - No requiere que el array esté ordenado
    
    Desventajas:
        - Lento para arrays grandes
        - Peor caso: O(n)
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


if __name__ == "__main__":
    # Ejemplos de uso
    
    # Ejemplo 1: Array pequeño
    numeros = [10, 25, 30, 45, 50, 70, 80, 90]
    print("Array:", numeros)
    
    # Búsqueda exitosa
    resultado = busqueda_lineal(numeros, 45)
    print(f"Buscar 45: índice {resultado}")
    
    resultado = busqueda_lineal(numeros, 25)
    print(f"Buscar 25: índice {resultado}")
    
    # Búsqueda fallida
    resultado = busqueda_lineal(numeros, 100)
    print(f"Buscar 100: índice {resultado}")
    
    # Ejemplo 2: Array de palabras
    print("\n" + "="*40)
    palabras = ["gato", "perro", "pajaro", "pez", "gusano"]
    print("Array:", palabras)
    
    resultado = busqueda_lineal(palabras, "pajaro")
    print(f"Buscar 'pajaro': índice {resultado}")
    
    resultado = busqueda_lineal(palabras, "leon")
    print(f"Buscar 'leon': índice {resultado}")

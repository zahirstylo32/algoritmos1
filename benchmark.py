"""
Benchmark de Rendimiento
Compara el rendimiento de diferentes algoritmos
"""

import time
import matplotlib.pyplot as plt
from busqueda_lineal import busqueda_lineal
from busqueda_binaria import busqueda_binaria
from elementos_unicos import elementos_unicos, elementos_unicos_optimizado
from multiplicacion_matrices import multiplicar_matrices


def test_busquedas():
    """
    Compara el rendimiento entre búsqueda lineal y binaria.
    """
    tamaños = [10, 50, 100, 200, 500, 1000]
    
    tiempos_lineal = []
    tiempos_binaria = []
    
    print("Probando búsquedas...")
    for n in tamaños:
        arr = list(range(n))
        x = n - 1  # Buscar el último elemento
        
        # Búsqueda lineal
        inicio = time.time()
        for _ in range(100):
            busqueda_lineal(arr, x)
        tiempos_lineal.append(time.time() - inicio)
        
        # Búsqueda binaria
        inicio = time.time()
        for _ in range(100):
            busqueda_binaria(arr, x)
        tiempos_binaria.append(time.time() - inicio)
    
    # Graficar resultados
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos_lineal, marker='o', label="Lineal O(n)")
    plt.plot(tamaños, tiempos_binaria, marker='s', label="Binaria O(log n)")
    plt.xlabel("Tamaño del array")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación: Búsqueda Lineal vs Binaria")
    plt.legend()
    plt.grid(True)
    plt.savefig("benchmark_busquedas.png")
    print("Gráfico guardado como 'benchmark_busquedas.png'")
    plt.show()


def test_elementos_unicos():
    """
    Compara el rendimiento entre la versión de fuerza bruta y optimizada.
    """
    tamaños = [10, 50, 100, 200, 300]
    
    tiempos_fuerza_bruta = []
    tiempos_optimizado = []
    
    print("\nProbando elementos únicos...")
    for n in tamaños:
        arr = list(range(n))
        
        # Fuerza bruta
        inicio = time.time()
        for _ in range(10):
            elementos_unicos(arr)
        tiempos_fuerza_bruta.append(time.time() - inicio)
        
        # Optimizado
        inicio = time.time()
        for _ in range(10):
            elementos_unicos_optimizado(arr)
        tiempos_optimizado.append(time.time() - inicio)
    
    # Graficar resultados
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos_fuerza_bruta, marker='o', label="Fuerza Bruta O(n²)")
    plt.plot(tamaños, tiempos_optimizado, marker='s', label="Optimizado O(n)")
    plt.xlabel("Tamaño del array")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación: Elementos Únicos")
    plt.legend()
    plt.grid(True)
    plt.savefig("benchmark_unicos.png")
    print("Gráfico guardado como 'benchmark_unicos.png'")
    plt.show()


def test_multiplicacion_matrices():
    """
    Mide el rendimiento de la multiplicación de matrices.
    """
    tamaños = [5, 10, 20, 30]
    tiempos = []
    
    print("\nProbando multiplicación de matrices...")
    for n in tamaños:
        A = [[i+j for j in range(n)] for i in range(n)]
        B = [[i+j for j in range(n)] for i in range(n)]
        
        inicio = time.time()
        for _ in range(5):
            multiplicar_matrices(A, B)
        tiempos.append(time.time() - inicio)
    
    # Graficar resultados
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos, marker='o', linewidth=2, markersize=8)
    plt.xlabel("Tamaño de la matriz (n x n)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Multiplicación de Matrices O(n³)")
    plt.grid(True)
    plt.savefig("benchmark_matrices.png")
    print("Gráfico guardado como 'benchmark_matrices.png'")
    plt.show()


if __name__ == "__main__":
    print("=== BENCHMARK DE ALGORITMOS ===\n")
    test_busquedas()
    test_elementos_unicos()
    test_multiplicacion_matrices()
    print("\n=== BENCHMARK COMPLETADO ===")

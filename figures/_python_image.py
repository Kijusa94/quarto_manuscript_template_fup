import matplotlib.pyplot as plt
import numpy as np

def plot_linear_function(m, b):
    # Generar valores de x
    x = np.linspace(-10, 10, 100)
    # Calcular valores de y = mx + b
    y = m * x + b

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'y = {m}x + {b}')
    
    # Configuración de los ejes
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.title('Gráfica de una Función Lineal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# Ejemplo de uso: y = 2x + 3
plot_linear_function(2, 3)
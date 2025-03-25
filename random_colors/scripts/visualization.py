import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    return pd.read_csv(filename)

def visualize_data(data):
    """Genera un scatter plot con etiquetas y leyenda."""
    plt.figure(figsize=(10, 6))
    colors = {'red': 'r', 'blue': 'b', 'green': 'g'}
    
    for color in colors:
        subset = data[data['color'] == color]
        plt.scatter(subset['x'], subset['y'], c=colors[color], label=color, alpha=0.6, edgecolors='k')
    
    plt.xlabel("Eje X (Valores Aleatorios)")
    plt.ylabel("Eje Y (Valores Aleatorios)")
    plt.title("Visualización de Datos - Scatter Plot")
    plt.legend(title="Colores")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    data = load_data('data/dataset.csv')
    visualize_data(data)
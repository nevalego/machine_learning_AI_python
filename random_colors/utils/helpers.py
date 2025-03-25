import numpy as np
import pandas as pd

def generate_sample_data(filename, num_samples=100):
    """
    Genera un dataset de ejemplo con columnas con valores numericos aleatorios.
    """
    np.random.seed(42)
    data = {
        'x': np.random.rand(num_samples) * 100,
        'y': np.random.rand(num_samples) * 100,
        'color': np.random.choice(['red', 'blue', 'green'], num_samples)
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Dataset generado y guardado en {filename}")

def load_data(filename):
    """Carga un dataset CSV y lo devuelve como un DataFrame."""
    return pd.read_csv(filename)

def summarize_data(data):
    """Devuelve estadísticas descriptivas del dataset."""
    return data.describe()

if __name__ == "__main__":
    generate_sample_data('data/dataset.csv')
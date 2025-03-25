import pandas as pd

def load_data(filename):
    return pd.read_csv(filename)

def analyze_data(data):
    summary_stats = data.describe()
    return summary_stats

if __name__ == "__main__":
    data = load_data('data/dataset.csv')
    analysis_result = analyze_data(data)
    print("Summary statistics:")
    print(analysis_result)
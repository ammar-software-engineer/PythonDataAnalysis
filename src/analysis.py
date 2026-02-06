import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_mean(df, column):
    return df[column].mean()

if __name__ == "__main__":
    # Example usage (assuming 'data.csv' exists)
    # data = load_data('data.csv')
    # print(f"Mean of 'value' column: {calculate_mean(data, 'value')}")
    print("Data analysis module loaded.")

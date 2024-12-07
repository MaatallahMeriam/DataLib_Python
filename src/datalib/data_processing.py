import pandas as pd

def load_csv(file_path):
    """
    Charge un fichier CSV dans un DataFrame.

    :param filepath: Le chemin du fichier CSV.
    :return: Un DataFrame contenant les données.
    """
    return pd.read_csv(file_path)

def save_csv(dataframe, file_path):
    """Enregistre un DataFrame dans un fichier CSV."""
    dataframe.to_csv(file_path, index=False)

def normalize_column(dataframe, column):
    """Normalise une colonne en utilisant Min-Max scaling."""
    min_val = dataframe[column].min()
    max_val = dataframe[column].max()
    dataframe[column] = (dataframe[column] - min_val) / (max_val - min_val)
    return dataframe

def handle_missing_values(dataframe, strategy="mean"):
    """Gère les valeurs manquantes selon une stratégie donnée."""
    if strategy == "mean":
        return dataframe.fillna(dataframe.mean())
    elif strategy == "median":
        return dataframe.fillna(dataframe.median())
    else:
        raise ValueError("Stratégie non reconnue : 'mean' ou 'median'.")

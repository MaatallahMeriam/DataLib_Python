from datalib.data_processing import load_csv, save_csv

# Charger un fichier CSV
df = load_csv("data.csv")

# Sauvegarder les données
save_csv(df, "output.csv")

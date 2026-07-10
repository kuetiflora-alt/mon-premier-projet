import sqlite3
import pandas as pd

print("--- Étape 1 : Connexion et création de la table ---")
# Connexion à la base de données
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

# On crée la table 'utilisateurs' pour être SÛR qu'elle existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        email TEXT
    )
''')

# On insère des données fictives pour le test
cursor.execute("DELETE FROM utilisateurs") # On vide d'abord pour repartir à zéro
donnees_test = [
    ('Alice', 'alice@example.com'),
    ('Bob', None),
    ('Alice', 'alice@example.com'),
    ('charles', 'charles@example.com')
]
cursor.executemany("INSERT INTO utilisateurs (nom, email) VALUES (?, ?)", donnees_test)
conn.commit()
print("Données de test insérées !")

print("\n--- Étape 2 : Lecture et nettoyage avec Pandas ---")
# Maintenant, Pandas ne peut plus dire que la table n'existe pas !
df = pd.read_sql_query("SELECT * FROM utilisateurs", conn)
print("Données brutes :\n", df)

# Nettoyage
df = df.drop(columns=['id']) 
df.drop_duplicates(inplace=True)
df.dropna(subset=['email'], inplace=True)
df['nom'] = df['nom'].str.upper()

print("\nDonnées nettoyées :\n", df)

# Sauvegarde finale
df.to_sql('utilisateurs', conn, if_exists='replace', index=False)
conn.close()
print("\n--- Opération réussie avec succès ! ---")
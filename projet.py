import pandas as pd

print("--- DEBUT DU NETTOYAGE MARKETING (EXCEL) ---")

try:
    # On ouvre le fichier avec la fonction dédiée à Excel
    df = pd.read_excel('Marketing.xlsx')
    print("Fichier Excel ouvert avec succès !")
    
    # Recalcul des colonnes corrompues par Excel
    df['Date'] = pd.to_datetime(df['Date'])
    df['CTR'] = ((df['Clicks'] / df['Impressions']) * 100).round(2)
    df['CPC'] = (df['Spend'] / df['Clicks']).round(2)
    df['ROAS'] = (df['Revenue'] / df['Spend']).round(2)

    # Nettoyage des textes
    for col in ['Canal', 'Campagne', 'Région', 'Device']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    print("\n--- Données recalculées et nettoyées ! ---")
    print(df[['Date', 'Canal', 'CTR', 'CPC', 'ROAS']].head())

    # Sauvegarde du résultat dans un fichier CSV tout propre
    df.to_csv('Marketing_Cleaned.csv', index=False)
    print("\nFichier 'Marketing_Cleaned.csv' créé dans votre dossier.")

except FileNotFoundError:
    print("Erreur : Le fichier 'Marketing.xlsx' est introuvable.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
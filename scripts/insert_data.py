import sqlite3


# Connexion à SQLite (ou création de la base si elle n'existe pas)
conn = sqlite3.connect('ma_base_de_donnees.db')

# Création d'un curseur pour exécuter des commandes SQL
cur = conn.cursor()

# Exemple : Création de la table entreprises
cur.execute('''
CREATE TABLE IF NOT EXISTS entreprises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    domaine TEXT,
    nombre_avis INTEGER,
    trustscore REAL
)
''')

# Commit des changements
conn.commit()

# Fermeture de la connexion
cur.close()
conn.close()

print("Table entreprises créée avec succès.")

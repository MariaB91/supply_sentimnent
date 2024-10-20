create table entreprises (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255),
    domaine VARCHAR(255),
    nombre_avis INT
    trustscore DECIMAL(3, 2)
)

create table avis (
    id SERIAL PRIMARY KEY,
    entreprise_id INT REFERENCES entreprise_id,
    utilisateur VARCHER(255),
    note INT CHECK (note BETWEEN 1 AND 5),
    texte TEXT,
    reponse_entreprise TEXT,
    
)
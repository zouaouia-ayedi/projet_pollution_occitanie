import sqlite3 # importer la bibliothèque "sqlite3"
import csv # importation de la bibliothèque pour importer en csv


#__________________________________________________________________________________________________________________________________________________



#Connexion à la base de donnée par un chemin relatif
connexion = sqlite3.connect("../BD/projet_statinfo.db")
cursor = connexion.cursor()


#__________________________________________________________________________________________________________________________________________________


#Exécution de la requête SQL
cursor.execute("""
                SELECT s.nom_com, AVG(p.valeur_poll) AS pollution_moyenne_2023, s.population_municipale_2023
                FROM mesures_occitanie_pollution as p
                INNER JOIN socio_economique as s ON p.code_insee = s.code_insee
                WHERE p.annee = 2023 AND s.population_municipale_2023 > 10000
                GROUP BY s.code_insee, s.nom_com, s.population_municipale_2023
                ORDER BY pollution_moyenne_2023 DESC;
               """)

#récupère les données
resultats = cursor.fetchall()


#__________________________________________________________________________________________________________________________________________________


#Importer les données dans un fichier CSV
with open("pollution_grandes_villes_2023.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")


    writer.writerow([
        "nom_commune",
        "pollution_moyenne_2023",
        "population_2023"
    ])

    # Données
    for nom_com, pollution, population in resultats:
        writer.writerow([
            nom_com,
            round(pollution, 2),
            population
        ])

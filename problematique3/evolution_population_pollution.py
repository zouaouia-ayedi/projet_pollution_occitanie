import sqlite3 # importer la bibliothèque "sqlite3"
import csv # importation de la bibliothèque pour importer en csv


#__________________________________________________________________________________________________________________________________________________



#Connexion à la base de donnée par un chemin relatif
connexion = sqlite3.connect("../BD/projet_statinfo.db")
cursor = connexion.cursor()


#__________________________________________________________________________________________________________________________________________________


#Exécution de la requête SQL
cursor.execute("""
                    SELECT s.evolution_2017_2023, AVG(p.valeur_poll) AS pollution_moyenne
                    FROM mesures_occitanie_pollution as p
                    INNER JOIN socio_economique as s ON p.code_insee = s.code_insee
                    GROUP BY s.code_insee
                    ORDER BY s.evolution_2017_2023 DESC;
               """)

#récupère les données
resultats = cursor.fetchall()


#__________________________________________________________________________________________________________________________________________________


#Importer les données dans un fichier CSV

with open("evolution_population_pollution.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")

   
    writer.writerow([
        "evolution_population_2017_2023",
        "pollution_moyenne"
    ])

    # Données
    for evolution, pollution in resultats:
        writer.writerow([
            evolution,
            round(pollution, 2)
        ])
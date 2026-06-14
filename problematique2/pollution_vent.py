import sqlite3 # importer la bibliothèque "sqlite3"
import csv # importation de la bibliothèque pour importer en csv


#__________________________________________________________________________________________________________________________________________________



#Connexion à la base de donnée par un chemin relatif
connexion = sqlite3.connect("../BD/projet_statinfo.db")
cursor = connexion.cursor()


#__________________________________________________________________________________________________________________________________________________


#Exécution de la requête SQL
cursor.execute("""
                    SELECT c.Force_vent_med, AVG(p.valeur_poll) AS pollution_moyenne
                    FROM mesures_occitanie_pollution as p
                    INNER JOIN geo_climatique as c ON p.code_insee = c.code_insee
                    GROUP BY c.Force_vent_med
                    ORDER BY c.Force_vent_med asc ; 
               """)

#récupère les données
resultats = cursor.fetchall()


#__________________________________________________________________________________________________________________________________________________


#Importer les données dans un fichier CSV
with open("pollution_vent.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")

    writer.writerow(["vent", "pollution_moyenne"])

    for vent, pollution in resultats:
        writer.writerow([
            vent,
            str(round(pollution, 2)).replace(".", ",")
        ])
        
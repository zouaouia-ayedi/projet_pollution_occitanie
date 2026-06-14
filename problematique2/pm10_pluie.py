import sqlite3 # importer la bibliothèque "sqlite3"
import csv # importation de la bibliothèque pour importer en csv


#__________________________________________________________________________________________________________________________________________________



#Connexion à la base de donnée par un chemin relatif
connexion = sqlite3.connect("../BD/projet_statinfo.db")
cursor = connexion.cursor()


#__________________________________________________________________________________________________________________________________________________


#Exécution de la requête SQL
cursor.execute("""
               SELECT ROUND(c.RR_med) AS pluie, AVG(p.valeur_poll) AS PM10
                FROM mesures_occitanie_pollution as p
                INNER JOIN geo_climatique as c ON p.code_insee = c.code_insee
                WHERE p.nom_poll = 'PM10'
                GROUP BY pluie
                ORDER BY pluie;
               """)

#récupère les données
resultats = cursor.fetchall()


#__________________________________________________________________________________________________________________________________________________


#Importer les données dans un fichier CSV

with open("pm10_pluie.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")

    writer.writerow(["pluie_RR_med", "PM10_moyen"])

    for pluie, pollution in resultats:
        writer.writerow([
            pluie,
            str(round(pollution, 2)).replace(".", ",")
        ])


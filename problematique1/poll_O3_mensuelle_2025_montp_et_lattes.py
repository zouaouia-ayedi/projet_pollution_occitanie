import sqlite3 # importer la bibliothèque "sqlite3"
import csv # importation de la bibliothèque pour importer en csv


#__________________________________________________________________________________________________________________________________________________



#Connexion à la base de donnée par un chemin relatif
connexion = sqlite3.connect("../BD/projet_statinfo.db")
cursur = connexion.cursor()


#__________________________________________________________________________________________________________________________________________________


#Exécution de la requête SQL
cursur.execute("""
               SELECT nom_com, nom_poll, mois, ROUND(AVG(valeur_poll),2) AS moyenne_pollution
                FROM mesures_occitanie_pollution
                WHERE (lower(nom_com) = 'montpellier' or lower(nom_com)= 'lattes') AND annee =2025 AND nom_poll ='O3'
                GROUP BY nom_com, nom_poll, mois ; """)

#récupère les données
resultats = cursur.fetchall()


#__________________________________________________________________________________________________________________________________________________


#Importer les données dans un fichier CSV
with open("O3_mensuelle_2025_montpellier_et_lattes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")

    writer.writerow(["nom_com", "nom_poll", "mois", "moyenne_pollution"])

    for nom_com, nom_poll, mois, moyenne in resultats:
        writer.writerow([
            nom_com, nom_poll, mois,  moyenne
        ])
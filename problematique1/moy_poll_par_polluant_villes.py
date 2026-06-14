import sqlite3 # importer la bibliothèque "sqlite3"
import csv # importation de la bibliothèque pour importer en csv


#__________________________________________________________________________________________________________________________________________________



#Connexion à la base de donnée par un chemin relatif
connexion = sqlite3.connect("../BD/projet_statinfo.db")
cursur = connexion.cursor()


#__________________________________________________________________________________________________________________________________________________


#Exécution de la requête SQL
cursur.execute("""
               SELECT nom_com, nom_poll, AVG(valeur_poll) AS moyenne
                FROM mesures_occitanie_pollution
                WHERE lower(nom_com) = 'montpellier' or lower(nom_com)= 'lattes'
                GROUP BY nom_com, nom_poll
                ORDER BY nom_com, moyenne desc ; """)

#récupère les données
resultats = cursur.fetchall()


#__________________________________________________________________________________________________________________________________________________


#Importer les données dans un fichier CSV
with open("moypoll_par_polluant_pour_mtp_et_lattes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")

    writer.writerow(["nom_com", "nom_poll", "moyenne"])

    for nom_com, nom_poll, moyenne in resultats:
        writer.writerow([
            nom_com, nom_poll, moyenne
        ])
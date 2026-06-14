import sqlite3 # importer la bibliothèque "sqlite3"
import csv # importation de la bibliothèque pour importer en csv


#_______________________________________________________________________________________________________________________________



#Connexion à la base de donnée grâce à une fonction
def connecter():
    connexion = sqlite3.connect("projet_statinfo.db")
    return connexion


#_______________________________________________________________________________________________________________________________



#Création de la Table Mesures_occitanie_pollution
def creer_la_table(con):

    #créer un curseur pour pouvoir insérer ma nouvelle table
    cursor = con.cursor()

    #Vérifier si la table existe déja la supprimer
    cursor.execute("DROP TABLE IF EXISTS mesures_occitanie_pollution;")

    cursor.execute("""CREATE TABLE IF NOT EXISTS mesures_occitanie_pollution (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nom_dept VARCHAR(100) NOT NULL,
               nom_com VARCHAR(100) NOT NULL,
               code_insee INT NOT NULL,
               nom_station VARCHAR(100),
               code_station VARCHAR(7),
               typologie VARCHAR(100),
               influence VARCHAR(100),
               nom_poll VARCHAR(20) NOT NULL,
               valeur_poll DECIMAL,
               jour INT CHECK(jour BETWEEN 1 AND 31),
               mois INT CHECK(mois BETWEEN 1 AND 12),
               annee INT CHECK(annee >= 2000),
               FOREIGN KEY (code_insee) REFERENCES socio_economique(code_insee),
               FOREIGN KEY (nom_com) REFERENCES geo_climatique(nom_com)
               ); """)
    
    con.commit()


#_______________________________________________________________________________________________________________________________



#fonction pour insérer les données dans ma table geo_climatique
def inserer_donnees(con, fichier_csv):

    #curseur pour exécuter dans la base de donnée 
    cursor = con.cursor()
    
    with open(fichier_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            cursor.execute("""
                           INSERT INTO mesures_occitanie_pollution(nom_dept, nom_com, code_insee,
                           nom_station, code_station, typologie, influence, nom_poll, valeur_poll, jour, mois, annee)
                           VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                           """, (
                               row["nom_dept"],row["nom_com"],row["code_insee_com"],row["nom_station"],row["code_station"],row["typologie"],
                               row["influence"],row["nom_poll"],row["valeur_poll"],row["jour"],row["mois"],row["annee"]
                               ))
            
    #sauvegarder les données
    con.commit()
    print("Données insérées avec succès !")


#_______________________________________________________________________________________________________________________________



#fonction principal
def main():
    print("Connexion à la base de donnée ----->")
    connexion = connecter()

    print("Création de la table mesures pollution occitanie.....")
    creer_la_table(connexion)

    print("Insertion des données...")
    inserer_donnees(connexion, "../donnees_fournis/donnees_mesures_occitanie_journaliere_pollution.csv")

    connexion.close()
    print("==> Base de donnée créée avec succès")


main()

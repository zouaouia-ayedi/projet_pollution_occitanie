import sqlite3 # importer la bibliothèque "sqlite3"
import csv # importation de la bibliothèque pour importer en csv


#_______________________________________________________________________________________________________________________________



#Connexion à la base de donnée grâce à une fonction
def connecter():
    connexion = sqlite3.connect("projet_statinfo.db")
    return connexion


#_______________________________________________________________________________________________________________________________



#Création de la Table Geo_climatique
def creer_la_table(con):

    #créer un curseur pour pouvoir insérer ma nouvelle table
    cursor = con.cursor()

    #Vérifier si la table existe déja la supprimer
    cursor.execute("DROP TABLE IF EXISTS geo_climatique;")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS geo_climatique (
               code_insee INT NOT NULL,
               nom_com VARCHAR(100) NOT NULL,
               reg_code INT,
               reg_nom VARCHAR(100),
               dep_code INT,
               dep_nom VARCHAR(100),
               population INT CHECK(population >= 0), 
               superficie_km2 INT CHECK(superficie_km2 >= 0), 
               densite INT CHECK(densite >= 0), 
               latitude DECIMAL,
               longitude DECIMAL, 
               densite_cat VARCHAR(100),
               alti_med INT,
               RR_med DECIMAL,
               NBJRR1_med INT,
               NBJRR5_med INT,
               NBJRR10_med INT,
               Tmin_med DECIMAL,
               Tmax_med DECIMAL,
               Tens_vap_med DECIMAL,
               Force_vent_med DECIMAL,
               Insolation_med DECIMAL,
               Rayonnement_med DECIMAL,
               PRIMARY KEY (code_insee, nom_com),
               CHECK(Tmin_med <= Tmax_med) 
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
                           INSERT INTO geo_climatique
                           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                           """, (
                               row["code_insee_com"],row["nom_com"],row["reg_code"],row["reg_nom"],row["dep_code"],row["dep_nom"],
                               row["population"],row["superficie_km2"],row["densite"],row["latitude"],row["longitude"],
                               row["densite_cat"],row["alti_med"],row["RR_med"],row["NBJRR1_med"],row["NBJRR5_med"],
                               row["NBJRR10_med"],row["Tmin_med"],row["Tmax_med"],row["Tens_vap_med"],row["Force_vent_med"],
                               row["Insolation_med"],row["Rayonnement_med"]
                               ))

    #sauvegarder les données
    con.commit()
    print("Données insérées avec succès !")


#_______________________________________________________________________________________________________________________________



#fonction principal
def main():
    print("Connexion à la base de donnée ----->")
    connexion = connecter()

    print("Création de la table géographie.....")
    creer_la_table(connexion)

    print("Insertion des données...")
    inserer_donnees(connexion, "../donnees_fournis/donnees_geo_climatiques.csv")

    connexion.close()
    print("==> Base de donnée créée avec succès")


main()



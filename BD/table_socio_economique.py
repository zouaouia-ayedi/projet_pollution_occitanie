import sqlite3 # importer la bibliothèque "sqlite3"
import csv # importation de la bibliothèque pour importer en csv


#_______________________________________________________________________________________________________________________________



#Connexion à la base de donnée grâce à une fonction
def connecter():
    connexion = sqlite3.connect("projet_statinfo.db")
    return connexion


#_______________________________________________________________________________________________________________________________



#Création de la Table Socio_economique
def creer_la_table(con):

    #créer un curseur pour pouvoir insérer ma nouvelle table
    cursor = con.cursor()

    #Vérifier si la table existe déja la supprimer
    cursor.execute("DROP TABLE IF EXISTS socio_economique;")

    cursor.execute("""CREATE TABLE IF NOT EXISTS  socio_economique (
               code_insee INT PRIMARY KEY,
               nom_com VARCHAR(100) NOT NULL,
               niveau_vie_median_2021 INT CHECK(niveau_vie_median_2021 >= 0),
               nb_logements_2022 INT CHECK(nb_logements_2022 >= 0),
               pourcentage_appartements_2022 DECIMAL CHECK((pourcentage_appartements_2022 BETWEEN 0 AND 100) OR pourcentage_appartements_2022 IS NULL ),
               pourcentage_locataires_dans_residence_principale_2022 DECIMAL CHECK(pourcentage_locataires_dans_residence_principale_2022 BETWEEN 0 AND 100),
               evolution_2017_2023 DECIMAL,
               population_municipale_2023 INT CHECK(population_municipale_2023 >= 0),
               taux_activite_tranche15_64_en_2022 DECIMAL CHECK(taux_activite_tranche15_64_en_2022 BETWEEN 0 AND 100)
               ); """)
    con.commit()


#_______________________________________________________________________________________________________________________________

#AVANT d'insérer les données pour ne pas causer de problème avec les contraintes (surtout avec le pourcentage)
def nettoyer_valeur(val):
    if val is None or val == "" or "N/A" in val:
        return None
    try:
        return float(val)
    except:
        return None
    


#fonction pour insérer les données dans ma table Socio_economique
def inserer_donnees(con, fichier_csv):

    #curseur pour exécuter dans la base de donnée 
    cursor = con.cursor()
    with open(fichier_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                           INSERT INTO socio_economique
                           VALUES (?,?,?,?,?,?,?,?,?)
                           """, (
                               row["code_insee_com"], row["nom_com"], nettoyer_valeur(row["niveau_vie_median_2021"]),
                               nettoyer_valeur(row["nb_logements_2022"]), nettoyer_valeur(row["Pourcentage_appartements_2022"]),
                               nettoyer_valeur(row["pourcentage_locataires_dans_résidence_principale_2022"]), 
                               nettoyer_valeur(row["evolution_annuelle_moy_de_la_population_entre_2017_et_ 2023_en_pourcentage"]),
                               nettoyer_valeur(row["population_municipale_2023"]), nettoyer_valeur(row["Taux_activite_tranche_15-64_en_2022"])
                               ))
                        
    #sauvegarder les données
    con.commit()
    print("Données insérées avec succès !")


#_______________________________________________________________________________________________________________________________



#fonction principal
def main():
    print("Connexion à la base de donnée ----->")
    connexion = connecter()

    print("Création de la table socio-economique.....")
    creer_la_table(connexion)

    print("Insertion des données...")
    inserer_donnees(connexion, "../donnees_fournis/donnees_socio_economiques.csv")

    connexion.close()
    print("==> Base de donnée créée avec succès")


main()

<?php
require("connect.php");
$connexion = mysqli_connect(SERVEUR, LOGIN, PASSE);
if (!$connexion) {
echo "Connexion à ".SERVEUR." impossible\n";
exit;
}
if (!mysqli_select_db($connexion,BASE)) {
echo "Accès à la base ". BASE ." impossible\n";
exit;
}
// echo "Connecté au SGBD MariaDB, à la base ". BASE ."\n";
mysqli_set_charset($connexion,"utf8");
$resultats_films = mysqli_query($connexion, "select * from MI0A401T_Films");
$error = "";
if (!$resultats_films) {
$error = mysqli_error($connexion);
}



$num = $_POST['NumFilm'];
$titre = $_POST['Titre'];
$real = $_POST['NumInd'];
$genre = $_POST['Genre'];
$annee = $_POST['Annee'];

$sql = "INSERT INTO MI0A401T_Films(NumFilm, Titre,NumInd, Genre, Annee)
        VALUES ('$num', '$titre', '$real', '$genre', '$annee')";

$resultats = mysqli_query($connexion, $sql);

if (!$resultats) {
    echo "Erreur : " . mysqli_error($connexion);
    echo "<br/>";
    echo "<a href='formulaire.html'>Retour au formulaire</a>";
} else {
    echo "L'ajout a été effectué.<br/>";
    echo "<a href='formulaire.html'>Retour au formulaire</a>";
}



$result = mysqli_query($connexion, "SELECT NumFilm, Titre FROM MI0A401T_Films");




?>



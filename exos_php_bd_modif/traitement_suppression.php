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

$result = mysqli_query($connexion, "SELECT NumFilm, Titre FROM MI0A401T_Films");


$titre = $_POST['Titre'];


?>



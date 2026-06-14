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

$resultats2 = mysqli_query($connexion,"SELECT NumFilm, Titre, Nom, Prenom
FROM  MI0A401T_Films
INNER JOIN MI0A401T_Individus using (NumInd)
WHERE genre ='Drame';");

?>


<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Liste des films</title>
<link rel="stylesheet" href="style/style.css"/>
</head>
<h2>Films de genre Drame</h2>
<?php
if ($error != "") {
echo "<p>Erreurs : $error</p>\n";
}
else {
    echo "<table>";
echo "<tr>\n";
echo "<th>Film</th>\n";
echo "<th>Titre</th>\n";
echo "<th>Réalisateur</th>\n";
echo "</tr>\n";
while ($film = mysqli_fetch_array($resultats2)) {
echo "<tr>";
echo "<td>".$film["NumFilm"]."</td>\n";
echo "<td>".$film["Titre"]."</td>\n";
echo "<td>".$film["Prenom"]." " .$film["Nom"]. "</td>\n";
echo "</tr>";
}
    echo "</table>";
}
?>
</body>
</html>
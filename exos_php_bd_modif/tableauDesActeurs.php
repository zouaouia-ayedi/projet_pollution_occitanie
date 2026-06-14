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

$resultats3 = mysqli_query($connexion,"SELECT I.NumInd, Nom, Prenom, count(NumFilm) as nbfilms
FROM MI0A401T_Individus as I
INNER JOIN MI0A401T_Acteurs using (NumInd)
GROUP BY I.NumInd;");

?>


<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Liste des films</title>
<link rel="stylesheet" href="style/style.css"/>
</head>
<h2>Acteurs</h2>
<?php
if ($error != "") {
echo "<p>Erreurs : $error</p>\n";
}
else {
    echo "<table>";
echo "<tr>\n";
echo "<th>numero</th>\n";
echo "<th>nom</th>\n";
echo "<th>prenom</th>\n";
echo "<th>nb films</th>\n";
echo "</tr>\n";

while ($film = mysqli_fetch_array($resultats3)) {
echo "<tr>";
echo "<td>".$film["NumInd"]."</td>\n";
echo "<td>".$film["Nom"]."</td>\n";
echo "<td>".$film["Prenom"]." " .$film["Nom"]. "</td>\n";
echo "<td>".$film["nbfilms"]."</td>\n";
echo "</tr>";
}
    echo "</table>";
}
?>
</body>
</html>
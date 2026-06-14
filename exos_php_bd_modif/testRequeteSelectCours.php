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
?>


<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Liste des films</title>
<link rel="stylesheet" href="style/style.css"/>
</head>
<body>
<h1>Cinémathèque ... </h1>
<h2>Liste des Films</h2>
<?php
if ($error != "") {
echo "<p>Erreurs : $error</p>\n";
}
else {
while ($film = mysqli_fetch_array($resultats_films)) {
echo "<p>".$film["NumFilm"].", de titre ".$film["Titre"]." du genre ".$film["Genre"]."</p>\n";
}
}
?>
</body>
</html>


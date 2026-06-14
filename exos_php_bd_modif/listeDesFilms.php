<?php
require("connect.php");
$connexion = mysqli_connect(SERVEUR, LOGIN, PASSE);
if (!$connexion) {
echo "Connexion à ".SERVEUR." impossible\n";
exit;
}
if (!mysqli_select_db($connexion,BASE)) {
echo "Accès à la base ".BASE." impossible\n";
exit;
}
// echo "Connecté au SGBD MariaDB, à la base ". BASE ."\n";
mysqli_set_charset($connexion,"utf8");
$resultats_films = mysqli_query($connexion, "select * from MI0A401T_Films");
$error = "";
if (!$resultats_films) {
$error = mysqli_error($connexion);
}

$genre= $_GET['genre'];
if ($genre == '*') {
    $sql = "SELECT NumFilm, Titre
    FROM MI0A401T_Films;";
} else {
    $sql = "SELECT NumFilm, Titre
    FROM MI0A401T_Films
    WHERE genre = '$genre';";
};

$resultats1 = mysqli_query($connexion,$sql);
?>




<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Liste des films</title>
<link rel="stylesheet" href="style/style.css"/>
</head>
<body>



<?php
if ($genre == "*"){
    echo "<h1> Films de tout les genres</h1>\n" ;}
else{
    echo "<h1> Films du genre $genre </h1>\n" ;
}
if ($error != "") {
echo "<p>Erreurs : $error</p>\n";
}
else {
    echo "<ul>\n";
    
    while ($film = mysqli_fetch_array($resultats1)) {
        echo "<li>".$film["NumFilm"]." - ".$film["Titre"]."</li>\n";
    }
    
    echo "</ul>\n";
}
echo "<p> <a href= 'choixFilms.html'>Retour au formulaire</a> </p>\n";
?>



</body>
</html>
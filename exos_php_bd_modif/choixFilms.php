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


$sql = "SELECT DISTINCT genre FROM MI0A401T_Films";
$resultats = mysqli_query($connexion, $sql);



?>




<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style/style.css">
</head>
<body>
    <h1>Cinémathèque ...</h1>

    <p>Ce formulaire vous permet de rechercher les films <strong>par leur genre</strong></p>
    
    <form action="listeDesFilms.php" method="get">

         Quel genre ?
         <select name="genre">
            <option value="*">*</option>

            <?php

            while ($ligne = mysqli_fetch_array($resultats)) {
            echo "<option value='".$ligne["genre"]."'>".$ligne["genre"]."</option>";
            }
            
            ?>
            
        </select>
        <input type="submit" value="Envoyer" />
    </form>

</body>
</html>
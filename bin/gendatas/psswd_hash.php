<?php

require './fonctions.php';


$pdo = new PDO('mysql:host=localhost;dbname=gsb_b3', 'userGsb', 'secret');
$visiteurs = getLesVisiteurs($pdo);

foreach ($visiteurs as $unVisiteur ) {
    $mdp = $unVisiteur['mdp'];
    $hashMdp = password_hash($mdp, PASSWORD_DEFAULT);
    $id = $unVisiteur['id'];
    $req = $pdo->prepare('UPDATE visiteur SET mdp= :hashMdp  WHERE id= :unId ');
    $req->bindParam(':hashMdp', $hashMdp, PDO::PARAM_STR);
    $req->bindParam(':unId', $id, PDO::PARAM_STR);
    $req->execute();
    echo 'le Mdp '. $mdp . 'de '. $unVisiteur['nom']. 'a été hasher =>' . $hashMdp . "\r\n";

}
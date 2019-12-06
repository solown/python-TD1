# python-TD1
Repository for TD1 in python - ENSIBS

Auteurs : Valentin BEYSSON - MAGNE Thibaud
Promotion : Cyberdéfense 1 - TD1
Version : 3.6.9

Logiciel de gestion de code utilisé : Atom et éditeur de texte Vim.
Logiciel de versionning de code : Git
Logiciel de dépôt de code : Github

Spécification des choix pour le main :
Un fichier en arguement quui est lu ligne par ligne et qui appele le main.
Le main permet de récupérer les différents arguments de la ligne, mais aussi de récupérer les erreurs en cas de problème au niveau du code ou au niveau de la fonction. 

La fonction split permet de récupérer les différents arguments en tant que liste pour les envoyer ensuite en entrée de la fonction.

On remplacera à chaque fois la dernière partie de la string qui contient un retour chariot (\n) avec un chaine vide ("") pour ne pas affecter le dernier arguement.

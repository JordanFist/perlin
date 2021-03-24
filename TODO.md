Objectifs pour une V0
======================

1. Generer une matrice de Perlin
    - la matrice doit contenir des nombres entre 0 et 1
    - trouver des conditions pour bien delimiter les couches
    - faire des visualisation avec des drawRect de Pygame

2. A partir d'une matrice de Perlin afficher une map 2D vue du dessus
    - utiliser une matrice qui contient des entiers (pas forcement de perlin) et attribuer chaque entier à une image
    - afficher la map

3. Poser un sprite sur la map qui est capable de se deplacer

4. Creer une camera qui fait bouger le background


Problemes d'optimisation
========================

1. Realiser un circularGradient entre les bornes min,max de notre matrice de perlin
2. Ne pas realiser de bijection et s'adapter au valeur min, max pour le passage à la map 2D
3. Reduire la sommation de bruit dans la fonction perlin si necessaire
4. TOFIX le joueur est plus rapide en diagonale car (triangle rectangle l'hypotenuse est plus grande que les cotes)

V1 idées
=========
1. Animer le sprite player
2. Creer une vraie camera (https://www.youtube.com/watch?v=GTxiCzvYNOc)
3. reflechir a une methode fullscreen
4. faire un title screen avec temps de chargement



V2 idées
========
1. Pouvoir aller sur l'eau
2. generer au dela du monde initial en tant reel
3. Ajouter des routes, villages, personnages
4. Ajouter de la musique et des sons


Aller plus loin
===============
1. Faire nous meme le code pour generer un bruit de perlin
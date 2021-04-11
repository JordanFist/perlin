Objectifs pour une V0
======================
1. Trouver un nouveau ressource pack

V1 idées
=========
1. Loading message -> Revoir la class Text
2. Vérifier collision quand on release le bouton
3. BouTons se replacent bien après le Re-Size


TOFIX : 
    Sur mac : 
        Sprite png noir (convert_alpha bordel)
    Sur windows : 
        Ne repaint pas au lancement du jeu





V2 idées
========
0. TROUVER CES PUTAINS DE SPRITES ! FAUT QU'ON ARRETE LES CONNERIES ! 
1. Villages, routes (Hora & Jo') :
    Villages : 
        Placer les villages : 
            - Améliorer l'algorithme pour placer les villages
            - Comment les placer sans les coller
    Chemins:
        Placer les chemins:
            - Algorithme A*
            - Algorithme Djikstra 
    
(2. Animation Personnage) ?

V3 idées
==========
1. Décoration sur île  : 
    - Buissons
    - Arbres
    - Rochers ...
2. Rivières
3. Ajouter de la musique et des sons


A Modifier
===========
1. Changer la manière dont on update les sprites utiliser la fonction update codée dans sprite.Sprite (https://www.youtube.com/watch?v=hDu8mcAlY4E&t=563s)

Aller plus loin
===============
1. Faire nous meme le code pour generer un bruit de perlin

Problemes d'optimisation
========================

1. Realiser un circularGradient entre les bornes min,max de notre matrice de perlin
2. Ne pas realiser de bijection et s'adapter au valeur min, max pour le passage à la map 2D
3. Reduire la sommation de bruit dans la fonction perlin si necessaire
4. Ne pas update toute la window mais seulement ce qui change à l'intérieur lorsque la camera est immobile

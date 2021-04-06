Objectifs pour une V0
======================
1. Trouver un nouveau ressource pack

V1 idées
=========
1. Animer le sprite player (Hora)
2. faire un title screen avec temps de chargement (Hora) : 
    - Bouton start
    - Loading bar




V2 idées
========
1. Pouvoir aller sur l'eau (Jo')
2. Villages, routes (Hora & Jo')
3. Settings pour title screen : (Hora)
    - SEED
    - MAP SCALE (comment faire ?) (comment redimmensionner la map pour pas que ca ne paraisse trop loin)

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

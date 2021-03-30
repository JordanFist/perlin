Objectifs pour une V0
======================
1. Trouver un nouveau ressource pack

V1 idées
=========
1. Animer le sprite player (Hora)
2. Creer une vraie camera (https://www.youtube.com/watch?v=GTxiCzvYNOc) (Jo')
3. Revoir l'ecran resizable avec la bonne caméra
    - le joueur va plus vite avec une plus petite window
    - lorsque la window est plus petite le joueur peut aller plus loin sur les bords et si on resize plus grand alors la view sort de la window et ca crash
    - Rajouter un GUI scale qui zoom la view si la window est trop grande utilisant des breakpoints pour savoir quand zoomer et dezoomer
4. faire un title screen avec temps de chargement (Hora) : 
    - Bouton start
    - Loading bar




V2 idées
========
1. Pouvoir aller sur l'eau (Jo')
2. Villages, routes (Hora & Jo')
3. Settings pour title screen : (Hora)
    - SEED
    - GUI SCALE

V3 idées
==========
1. Décoration sur île  : 
    - Buissons
    - Arbres
    - Rochers ...
2. Rivières
3. Ajouter de la musique et des sons




Aller plus loin
===============
1. Faire nous meme le code pour generer un bruit de perlin

Problemes d'optimisation
========================

1. Realiser un circularGradient entre les bornes min,max de notre matrice de perlin
2. Ne pas realiser de bijection et s'adapter au valeur min, max pour le passage à la map 2D
3. Reduire la sommation de bruit dans la fonction perlin si necessaire
4. TOFIX le joueur est plus rapide en diagonale car (triangle rectangle l'hypotenuse est plus grande que les cotes)

# SasVelo
Mesure du taux d'automobilistes ne respectant pas le sas vélo.


## Définition

Un sas cyclable, sas vélo ou zone avancée pour cyclistes est un espace réservé aux cyclistes, entre la ligne d'arrêt des véhicules et un passage piéton à un carrefour à feux tricolores. (Wikipedia)


## Jeu de données

Le jeu de données est constitué de photos d'un carrefour, prise à chaque cycle de feu, avant que le feu ne passe au vert. Elle ont été enregistrées grâce à un raspberry pi et sont disponibles [ici](https://drive.google.com/file/d/1-yFv0FQlNqnNtTcP_STJXKYqNGWPOW65/view?usp=sharing).
Les données peuvent être étiquetées à la main grâce au script [labelData.py](labelData.py). Les labels suivants sont utilisés:
```
0 : pas de voiture arrétée au feu
1 : voiture arrétée avant le sas vélo
2 : voiture arrétée dans le sas vélo (infraction)
```


## Réseau de neurones convolutif

Une réseau de neurones convolutif (CNN) est utilisé pour classifier les images selon les 3 labels définis. La mise en forme des données, ainsi que l'entrainement et la validation du CNN sont réalisé avec [CNN.ipynb](CNN.ipynb).


## Analyse statistique

Le CNN entrainé est utilisé pour prédire le label de toutes les données. Le taux d'infraction est ensuite mesuré avec l'incertitude (statistique) correspondante en construisant une fonction de vraisemblance prenant en compte la matrice de confusion du CNN, et en maximisant cette fonction.
Cette analyse est développée dans [analyse.ipynb](analyse.ipynb).

![](infraction_day.png?raw=true)
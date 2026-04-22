# Groupe fondamental des surfaces compactes

Ce dépôt contient un PDF consacré au calcul du groupe fondamental de trois
surfaces compactes classiques :

- le tore $T^2$
- le plan projectif réel ℝP²
- la bouteille de Klein $K$

ainsi qu'un script Python permettant de les visualiser dans l'espace à 3 dimensions.

Chaque surface est réalisée comme quotient du carré $[0,1]^2$ par identification
des bords, et le groupe fondamental est calculé par application du théorème de
Van Kampen.

Auteur : Lounis Boudaoud, étudiant en L2 à Sorbonne Université.

Période : mars – avril 2026

## Contenu du dépôt

- `Groupe_surfaces_compactes.pdf` : document principal (~11 pages).
- `latex/` : sources LaTeX du document, avec les figures.
- `visualisations.py` : script Python de visualisation des trois surfaces.
- `torus.gif`, `rp2.gif`, `klein.gif`, `klein8.gif` : animations montrant la transformation du carré en la surface correspondante.

## Résumé des résultats

Le tore est identifié au groupe $\langle a, b \mid aba^{-1}b^{-1} = 1 \rangle$, isomorphe à ℤ².

Pour le plan projectif réel, on a $\langle a \mid a^2 = 1 \rangle$, isomorphe à ℤ/2ℤ.

Pour la bouteille de Klein, $\langle a, b \mid aba^{-1}b = 1 \rangle$, dont on étudie quelques propriétés.

## Utilisation du script Python

Le script n'utilise que deux bibliothèques externes : `numpy` et `matplotlib`.

### Lancement

Depuis le dossier contenant le script et les GIFs :

```bash
python visualisations.py
```

Un menu interactif propose deux modes :

1. Lire un GIF pré-généré : ouvre l'animation du carré vers la surface
   avec le lecteur d'images par défaut du système. Pour la bouteille de Klein,
   deux représentations sont disponibles (forme "bouteille" classique et
   immersion en figure-8).
2. Calculer et afficher une surface : génère en direct une paramétrisation
   3D de la surface choisie et ouvre une fenêtre `matplotlib` permettant de
   la faire tourner à la souris.

Le plan projectif et la bouteille de Klein n'admettent pas de plongement dans
ℝ³, leur représentation 3D présente donc nécessairement des
auto-intersections.

## Référence principale

Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.
Chapitres utilisés : 1.1 (groupe fondamental) et 1.2 (théorème de Van Kampen).
Disponible librement sur [math.cornell.edu/~hatcher](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html).

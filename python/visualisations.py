# Script permettant de visualiser des surfaces en 3d ou via des gif pré-générés

import os
import platform
import subprocess
import numpy as np
import matplotlib.pyplot as plt


# Paramétrisations des surfaces

def tore(u, v):
    R, r = 2.0, 0.7
    theta = 2 * np.pi * u
    phi = 2 * np.pi * v
    x = (R + r * np.cos(phi)) * np.cos(theta)
    y = (R + r * np.cos(phi)) * np.sin(theta)
    z = r * np.sin(phi)
    return x, y, z


def plan_projectif(u, v):
    alpha = np.pi * u
    beta = np.pi * v
    x = 1.5 * np.sin(alpha) * np.sin(2 * beta)
    y = 1.5 * np.sin(2 * alpha) * np.cos(beta) ** 2
    z = 1.5 * np.cos(2 * alpha) * np.cos(beta) ** 2
    return x, y, z


def klein(u, v):
    R, r = 2.0, 0.6
    theta = 2 * np.pi * u
    phi = 2 * np.pi * v
    sec_r = np.cos(theta / 2) * np.sin(phi) - np.sin(theta / 2) * np.sin(2 * phi)
    sec_z = np.sin(theta / 2) * np.sin(phi) + np.cos(theta / 2) * np.sin(2 * phi)
    x = (R + r * sec_r) * np.cos(theta)
    y = (R + r * sec_r) * np.sin(theta)
    z = r * sec_z
    return x, y, z


# Calcul et affichage


def afficher(parametrisation, titre):
    N = 60
    u = np.linspace(0, 1, N)
    v = np.linspace(0, 1, N)
    U, V = np.meshgrid(u, v)
    x, y, z = parametrisation(U, V)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis', alpha=0.9, edgecolor='none')
    ax.set_title(titre)
    ax.set_box_aspect([1, 1, 1])
    plt.show()


def ouvrir_gif(fichier):
    if not os.path.exists(fichier):
        print(f"Fichier introuvable : {fichier}")
        return
    if platform.system() == "Windows":
        os.startfile(fichier)
    elif platform.system() == "Darwin":
        subprocess.run(["open", fichier])
    else:
        subprocess.run(["xdg-open", fichier])


SURFACES_CALCUL = {
    "1": ("Tore T²",               tore),
    "2": ("Plan projectif RP²",    plan_projectif),
    "3": ("Bouteille de Klein",    klein),
}


# Récupération du dossier contenant le script (pour retrouver les gifs)


DOSSIER_SCRIPT = os.path.dirname(os.path.abspath(__file__))

SURFACES_GIF = {
    "1": ("Tore T²",                              os.path.join(DOSSIER_SCRIPT, "torus.gif")),
    "2": ("Plan projectif RP²",                   os.path.join(DOSSIER_SCRIPT, "rp2.gif")),
    "3": ("Bouteille de Klein (bouteille)",       os.path.join(DOSSIER_SCRIPT, "klein.gif")),
    "4": ("Bouteille de Klein (figure-8)",        os.path.join(DOSSIER_SCRIPT, "klein8.gif")),
}

# Menu interactif


def menu_gif():
    print("\nGIFs disponibles :")
    for cle, (nom, _) in SURFACES_GIF.items():
        print(f"  {cle}. {nom}")
    choix = input("Choix : ").strip()
    if choix in SURFACES_GIF:
        _, fichier = SURFACES_GIF[choix]
        ouvrir_gif(fichier)
    else:
        print("Choix invalide.")


def menu_calcul():
    print("\nSurfaces à calculer :")
    for cle, (nom, _) in SURFACES_CALCUL.items():
        print(f"  {cle}. {nom}")
    choix = input("Choix : ").strip()
    if choix in SURFACES_CALCUL:
        nom, fonction = SURFACES_CALCUL[choix]
        afficher(fonction, nom)
    else:
        print("Choix invalide.")


def main():
    while True:
        print("\nQue voulez-vous faire ?")
        print("  1. Lire un GIF pré-généré")
        print("  2. Calculer et afficher une surface")
        print("  q. Quitter")
        mode = input("Choix : ").strip().lower()
        if mode == "1":
            menu_gif()
        elif mode == "2":
            menu_calcul()
        elif mode == "q":
            print("Au revoir.")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
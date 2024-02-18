  # importation de la classe Noeud d'un ABR
import arbre_binaire_recherche as abr

# importation de la bibliothèque Expressions Régulières
import re

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def calculer_frequence(texte, mots_reference):
    mots = re.findall(r'\b\w+\b', texte.lower())
    total_mots = len(mots)
    compteurs = Counter(mots)
    frequence = {mot: (compteurs[mot] / total_mots) * 10000 for mot in mots_reference}
    return frequence

# Mots de référence
auteurs = ["Victor Hugo", "George Sand", "Marcel Proust", "Colette"]
mots_reference = ["homme", "femme", "beau", "même", "très", "aussi", "donc", "car", "dieu", "amour"]
oeuvres = {
    "Victor Hugo": "quatreving-treize.txt",
    "George Sand": "la_mare_au_diable.txt",
    "Marcel Proust": "du_cote_de_chez_swann.txt",
    "Colette": "le_ble_en_herbe.txt"
}

# Dictionnaire pour stocker les résultats
resultats = {auteur: {} for auteur in auteurs}

# Calcul de la fréquence pour chaque auteur
for auteur, fichier in oeuvres.items():
    with open(fichier, 'r', encoding='utf-8') as file:
        texte = file.read()
        resultats[auteur] = calculer_frequence(texte, mots_reference)

# Création du graphique
fig, ax = plt.subplots()
bar_width = 0.2
index = np.arange(len(mots_reference))
bar_offsets = np.linspace(-0.3, 0.3, len(auteurs))  # Décalage des barres pour chaque auteur
colors = plt.cm.get_cmap('cool', len(auteurs))  # Palette de couleurs

for i, auteur in enumerate(auteurs):
    values = [resultats[auteur][mot] for mot in mots_reference]
    ax.bar(index + bar_offsets[i], values, bar_width, color=colors(i), label=auteur)

ax.set_xlabel('Mots de Référence')
ax.set_ylabel('Fréquence (x 10,000)')
ax.set_title('Fréquence des mots par auteur')
ax.set_xticks(index)
ax.set_xticklabels(mots_reference)

# Adjust the font size of the x-axis labels
ax.tick_params(axis='x', labelsize=7)

ax.legend(title='Auteurs', loc='upper left', bbox_to_anchor=(1, 1))

plt.show()

def index_roman(file):
    ''' Cette fonction crée un arbre binaire de recherche à partir
    d'un fichier texte, en classant les mots par ordre alphabétique.
    Paramètre d'entrée : un fichier texte
    Sortie : un ABR'''
    # récupération du texte dans le fichier
    texte = open(file,'r',encoding = 'utf-8')
    tableau = texte.readlines()
    texte.close()
        
    # initialisation de l'arbre binaire de recherche
    arbre = None

    # Boucle : pour chaque ligne du texte
    for ligne in tableau:
        # formatage du fichier texte
        # passage en minuscule
        ligne = ligne.lower()
        # on récupère une liste de mots, en enlevant tous les séparateurs connus
        liste_mots = re.split('[;_,.?!\"\'\-\%\n() `&«»]', ligne)
        # on enlève les mots vides dans la liste de mots
        while '' in liste_mots:
            liste_mots.remove('')
        
        # pour chaque mot dans la liste de mots
        for element in liste_mots:
            if arbre == None:
                arbre = abr.Noeud(liste_mots[0])
            else:
                arbre.inserer(element)
            
    return arbre

arbreBillie = index_roman("therefore_i_am.txt")
arbre80jours = index_roman("le_tour_du_monde_en_80_jours.txt")
arbre93 = index_roman("quatreving-treize.txt")
arbreBle = index_roman("le_ble_en_herbe.txt")
arbreDiable = index_roman("la_mare_au_diable.txt")
arbreSwann = index_roman("du_cote_de_chez_swann.txt")
arbre_infixe = []

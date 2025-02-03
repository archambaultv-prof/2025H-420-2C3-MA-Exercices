# Exercices de la semaine 2

# Les exercices sont accompagnés de tests unitaires pour vérifier votre
# solution. Vous pouvez exécuter les tests avec le package pytest.

import numpy as np


# Tableau vide []
tab1 = None


# Tableau de 20 zéros avec np.zeros()
tab2 = None


# Tableau de 18 uns avec np.ones()
tab3 = None


# Tableau de 3 dix avec np.ones()
tab4 = None


# Tableau aléatoire de 10 chiffres entre 0 et 1 avec np.random
tab5 = None


# Tableau aléatoire de 3 chiffres entre 5 et 10 avec np.random
tab7 = None


# Matrice 4x2 de zéros avec np.zeros
tab8 = None


# Matrice 10x5 de uns avec np.ones
tab9 = None


# Matrice 6x6 avec comme valeur de diagonale 10. Utiliser np.eye
tab10 = None


# Tableau avec éléments entiers de 15 à 100
tab11 = None


# Tableau avec éléments pairs de 20 à 80, les bornes excluses
tab12 = None


# Tableau avec 100 éléments entre 0 et 5 tirés aléatoirement
tab13 = None


# Écrire une fonction qui trouvera les indices des éléments égaux au paramètre
# X dans un tableau donné. La fonction doit retourner un tableau numpy avec les
# indices trouvés. Si aucun élément n'est trouvé, la fonction doit retourner un
# tableau vide.
def valeurs_X(tableau, X):
    pass


# Ecrivez un programme numpy pour convertir les valeurs des kilogrammes en
# livres. Les valeurs en kilogrammes sont stockées dans un tableau numpy.
# Formule de conversion : L = K * 2.20462. Ne pas utiliser de boucles !
def kilogramme_livre(kilogrammes):
    pass


# Ecrivez un programme NumPy pour trouver les valeurs qui ne sont pas communes
# entre deux tableaux donnés. Si vous cherchez bien dans la documentation
# officielle Numpy, vous trouverez une fonction qui fait ça en une seule ligne.
# Sinon, vous pouvez écrire votre propre fonction.
def valeurs_non_communes(tab1, tab2):
    pass


# Vous avez un tableau de notes d'étudiants et vous devez calculer les
# statistiques suivantes :
# Moyenne : La moyenne des notes.
# Médiane : La valeur médiane des notes.
# Écart-type : Une mesure de la dispersion des notes par rapport à la moyenne.
# Votre fonction doit retourner un dictionnaire avec ces statistiques.
# Les clés du dictionnaire sont 'moyenne', 'mediane' et 'ecart_type'.
def statistiques_notes(notes):
    pass

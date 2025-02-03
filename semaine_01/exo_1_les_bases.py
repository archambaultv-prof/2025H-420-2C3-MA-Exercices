# Exercices de la semaine 1

# Les exercices sont accompagnés de tests unitaires pour vérifier votre
# solution. Vous pouvez exécuter les tests avec le package pytest.


# Écrire une fonction qui accepte un nombre entier et retourne True si le
# les nombre est entre 0 et 100, sinon False.
def nombre_entre_zero_et_cent(n: int) -> bool:
    pass


# Écrire une fonction qui accepte un nombre entier et retourne True si le
# nombre est un multiple de 2 ou 5, sinon False.
def multiple_deux_ou_cinq(n: int) -> bool:
    pass


# Écrire une fonction qui accepte un nombre entier n et retourne une liste de
# listes représentant une table de multiplication de n x n. Par exemple, si n
# est 3, la fonction doit retourner:
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]] qui représente la table de multiplication
# [[1 * 1, 1 * 2, 1 * 3],
#  [2 * 1, 2 * 2, 2 * 3],
#  [3 * 1, 3 * 2, 3 * 3]]
def table_multiplication(n: int) -> list:
    pass


# Écrire une fonction qui accepte une chaîne de caractères et qui retourne une
# adresse courriel. Les informations prénom, nom et domaine sont séparées par
# des virgules. Par exemple, si la chaîne est "Alice,Bouchard,example.com", la
# fonction doit retourner "alice.bouchard@example.com". L'adresse courriel doit
# être en minuscules.
def adresse_courriel(s: str) -> str:
    pass


# Écrire une fonction qui calcule la liste des nombres pairs entre 0 et n
# inclusivement. Par exemple, si n est 10, la fonction doit retourner
# [0, 2, 4, 6, 8, 10].

# Utiliser une boucle while
def nombres_pairs_while(n: int) -> list:
    pass


# Utiliser une boucle for
def nombres_pairs_for(n: int) -> list:
    pass


# Écrire une fonction qui accepte deux listes et retourne une liste contenant
# des tuples avec les éléments correspondants des deux listes. Par exemple, si
# les deux listes sont [1, 2, 3] et ['a', 'b', 'c'], la fonction doit
# retourner [(1, 'a'), (2, 'b'), (3, 'c')]. Si les listes n'ont pas la même
# longueur, la fonction doit retourner autant de tuples que possible.
def zip_listes(liste1: list, liste2: list) -> list:
    pass


# Écrire une fonction qui, à partir de deux listes de nombres, retourne une 3e
# liste comprenant uniquement les nombres qui se retrouvent dans les deux
# premières listes.
def intersection_listes(liste1: list, liste2: list) -> list:
    pass


# Écrire une fonction qui accepte deux listes et retourne la liste des éléments
# en commun entre les deux listes, mais sans doublons. Par exemple, si les deux
# listes sont [1, 2, 2, 3] et [2, 3, 4], la fonction doit retourner [2, 3].
def intersection_listes_sans_doublons(liste1: list, liste2: list) -> list:
    pass


# Écrire une fonction qui accepte une liste de nombres et retourne la somme de
# tous les éléments de la liste. Si la liste est vide, la fonction doit
# retourner 0. Utiliser une boucle for.
def somme_liste(liste: list) -> int:
    pass

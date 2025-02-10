# Remplacer pass par votre code

from functools import reduce


# Redéfinir la fonction reduce en utilisant une boucle for
def my_reduce(func, list):
    acc = list[0]
    for i in list[1:]:
        acc = func(acc, i)
    return acc


# Utiliser la fonction reduce pour additionner les éléments de la liste
def sum_list(list):
    def add(x, y):
        return x + y
    return reduce(add, list)


# Utiliser la fonction reduce pour multiplier les éléments de la liste
def prod_list(list):
    return reduce(lambda x, y: x * y, list)


# Utiliser la fonction reduce pour trouver le maximum de la liste
def max_list(list):
    return reduce(lambda x, y: x if x > y else y, list)


# Plus difficile, mais vous pouvez le faire !
# Utiliser la fonction reduce pour écrire la fonction map
def my_map(func, list):
    def map_func(acc, x):
        acc.append(func(x))
        return acc
    # Le troisième argument de reduce est la valeur initiale de l'accumulateur
    return reduce(map_func, list, [])

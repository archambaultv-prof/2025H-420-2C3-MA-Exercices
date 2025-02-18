# Remplacer pass par votre code


# Redéfinir la fonction map en utilisant une boucle for
def my_map(func, list):
    ls = []
    for i in list:
        ls.append(func(i))
    return ls


# Utiliser la fonction map pour doubler les éléments de la liste
def double_list(list):
    def double(x):
        return x * 2
    return map(double, list)


# Utiliser la fonction map pour transformer les éléments de la liste en chaînes
# de caractères
def str_list(list):
    return map(str, list)

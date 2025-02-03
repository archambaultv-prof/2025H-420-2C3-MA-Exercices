# Remplacer pass par votre code


# Redéfinir la fonction filter en utilisant une boucle for
def my_filter(func, list):
    pass


# Utiliser la fonction filter pour conserver les éléments pairs de la liste
def even_list(list):
    pass

###############################################################################
# Réécrire les fonctions suivantes en utilisant les compréhensions de liste
###############################################################################


def bar(list):
    filter(lambda x: x % 2 == 0, list)


def foo(list):
    map(lambda x: x + 2, filter(lambda x: x % 2 == 1, list))


def baz(list):
    xs = []
    for x in list:
        for y in range(x):
            xs.append(y)
    return xs


def qux(list):
    xs = []
    for x in list:
        for y in range(x):
            if (x + y) % 2 == 0:
                xs.append(y)
    return xs

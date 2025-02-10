# Remplacer pass par votre code


# Redéfinir la fonction filter en utilisant une boucle for
def my_filter(func, list):
    ls = []
    for i in list:
        if func(i):
            ls.append(i)
    return ls


# Utiliser la fonction filter pour conserver les éléments pairs de la liste
def even_list(list):
    return my_filter(lambda x: x % 2 == 0, list)

###############################################################################
# Réécrire les fonctions suivantes en utilisant les compréhensions de liste
###############################################################################


def bar(list):
    # filter(lambda x: x % 2 == 0, list)
    return [x for x in list if x % 2 == 0]


def foo(list):
    # map(lambda x: x + 2, filter(lambda x: x % 2 == 1, list))
    return [x + 2 for x in list if x % 2 == 1]


def baz(list):
    # xs = []
    # for x in list:
    #     for y in range(x):
    #         xs.append(y)
    # return xs
    return [y for x in list for y in range(x)]


def qux(list):
    # xs = []
    # for x in list:
    #     for y in range(x):
    #         if (x + y) % 2 == 0:
    #             xs.append(y)
    # return xs
    return [y for x in list for y in range(x) if (x + y) % 2 == 0]

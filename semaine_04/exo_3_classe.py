# Mise en pratique de la méthode d'héritage coopératif.

# Cette classe n'est pas faite pour être instanciée, elle sert de classe mère
# pour les autres classes. Elle assume qu'un attribut `nom` est présent dans
# les classes filles
class Log:
    def log(self, message):
        print(f"Log: {self.nom}: {message}")


# Créez une classe `Transport` avec un attribut `nom`. Implémentez la méthode
# __init__ pour initialiser cet attribut.
class Transport:
    def __init__(self, nom):
        pass


# # Créez une classe `Velo` qui hérite des classes `Transport` et `Log`.
# # Implémentez la méthode __init__ pour initialiser les attributs de ces
# # classes. Vous devez fournir à transport un nom pour l'initialisation.
# class Velo(Transport, Log):
#     def __init__(self, type_velo):
#         pass


# # Exemple d'utilisation
# if __name__ == "__main__":
#     mon_velo = Velo("Montagne")
#     mon_velo.log("Ceci est un message de log pour le vélo.")

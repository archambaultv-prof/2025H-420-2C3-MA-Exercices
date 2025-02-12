
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        """Méthode abstraite"""
        pass


#  Un chien fait "Wouf"
class Chien(Animal):
    def parler(self):
        pass


# Un chat fait "Miaou"
class Chat(Animal):
    def parler(self):
        pass


# Exemple d'utilisation
if __name__ == "__main__":
    animaux: list[Animal] = [Chien("Rex"), Chat("Minou")]
    for animal in animaux:
        animal.parler()

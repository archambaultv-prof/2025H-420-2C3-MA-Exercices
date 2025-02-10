# Créez une classe `Personne` avec les attributs `prenom`, `nom` et `age`.
# Implémentez la méthode __init__ pour initialiser ces attributs. La classe
# `Personne` doit avoir une méthode `dire_bonjour` qui affiche "Bonjour, je
# m'appelle [prenom] [nom] et j'ai [age] ans."
class Personne:
    pass


# Créez une classe `Etudiant` qui hérite de la classe `Personne` avec en plus
# un paramètre optionnel `note` (par défaut 'Non attribuée'). Implémentez la
# méthode __init__ pour initialiser ces attributs.
class Etudiant:
    pass


# Créez une classe `Employe` qui hérite de la classe `Personne` avec en plus un
# paramètre optionnel `poste` (par défaut 'Employé'). Implémentez la méthode
# __init__ pour initialiser ces attributs. Implémentez une méthode `travailler`
# qui affiche "Je suis [prenom] [nom] et je suis [poste]." si le poste est
# différent de 'Employé' et "Je suis [prenom] [nom] et je suis un employé."
class Employe:
    pass


# Créez une classe `Stagiaire` qui hérite de la classe `Personne`, `Etudiant`
# et `Employe`. Attention il s'agit d'un héritage en diamant. La classe
# `Personne` ne doit pas être initialisée deux fois. Vous pouvez ajouter un
# `print` dans la méthode __init__ de `Personne` pour vérifier si elle est
# initialisée deux fois. Vous aurez peut-être besoin de modifier les classes
# `Personne`, `Etudiant` et `Employe` pour utiliser la méthode d'héritage
# coopératif.
class Stagiaire(Personne, Etudiant, Employe):
    pass

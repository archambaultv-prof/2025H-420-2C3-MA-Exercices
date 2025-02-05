# Programmation objet - Hiver 2025 - Collège de Maisonneuve

Ce dépôt contient les exercices du cours de programmation objet 420-2C3-MA donné
au [Collège de Maisonneuve](https://www.cmaisonneuve.qc.ca/) par le professeur
Vincent Archambault-Bouffard. Tout le monde est le bienvenue pour utiliser ce
contenu. 

## Site web du cours
- Le site web du cours est accessible via github pages à l'adresse
  [https://archambaultv-prof.github.io/2025H-420-2C3-MA](https://archambaultv-prof.github.io/2025H-420-2C3-MA).

## Comment utiliser ce dépôt

### Cloner le dépôt
Pour cloner ce dépôt, vous pouvez utiliser la commande suivante:
```bash
git clone https://github.com/archambaultv-prof/2025H-420-2C3-MA-Exercices.git
```

### Configurez votre environnement de développement
Vous pouvez vous référer au fichier [`config_exercices.md`](config_exercices.md)
pour configurer votre environnement de travail.

### Faire les exercices
Les exercices sont divisés par semaine. Chaque semaine contient différents
fichiers d'exercices. Pour chaque exercice, vous devez compléter le code dans le fichier.

### Utiliser pytest pour vous corriger
Plusieurs dossier hebdomadaire contiennent des tests unitaires. Ceux-ci vous
permettent de vérifier si votre code fonctionne correctement. Pour exécuter les
tests unitaires, depuis le terminal de VSCode, exécutez la commande suivante:

```bash
pytest
```

N'oublier pas d'activer votre environnement virtuel avant d'exécuter cette
commande. Normalement, pytest va trouver les tests unitaires et les exécuter
automatiquement. 

Il est possible que pytest retourne beaucoup d'erreurs. C'est normal si vous n'avez pas
encore complété les exercices. Pour dire à pytest d'exécuter seulement les tests
d'un fichier, vous pouvez spécifier le nom du fichier. Par exemple, pour exécuter
seulement les tests du fichier `semaine_01\test_exercice_1.py`, vous pouvez exécuter la
commande suivante:

```bash
pytest semaine_01\test_exercice_1.py
```

Vous pouvez aussi demander à pytest de n'afficher que la première erreur
qu'il trouve. Pour ce faire, vous pouvez ajouter l'option `-x` à la commande
`pytest`. Par exemple:

```bash
pytest -x
```


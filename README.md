# WriteNow

Prototype d'autocorrecteur global pour Windows.

## Utilisation

1. Installer les dépendances :

   ```bash
   pip install keyboard pyspellchecker
   ```

2. Exécuter le script `autocorrect.py`.

3. Tapez du texte dans n'importe quelle application : à chaque appui sur la barre d'espace, le mot précédent est comparé à un dictionnaire local et éventuellement remplacé par la meilleure suggestion.

Le script utilise la bibliothèque `keyboard` pour intercepter les frappes et [`pyspellchecker`](https://github.com/barrust/pyspellchecker) pour la recherche de la correction la plus probable sans appel à un service externe.

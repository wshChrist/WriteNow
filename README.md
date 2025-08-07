# WriteNow

Prototype d'autocorrecteur global pour Windows.

## Utilisation

1. Installer les dépendances :

   ```bash
   pip install keyboard language_tool_python
   ```

2. Exécuter le script `autocorrect.py`.

3. Tapez du texte dans n'importe quelle application : à chaque espace ou ponctuation, le mot précédent est analysé et corrigé automatiquement.

Le script repose sur [LanguageTool](https://languagetool.org/) pour la correction en français et utilise la bibliothèque `keyboard` pour intercepter les frappes.

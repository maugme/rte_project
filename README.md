# RTE Project

## Introduction
Ce projet contient des propositions de réponses pour deux exercices techniques. L'un évalue l'utilisation de `FastAPI` et des fonctions asynchrones. L'autre a pour but d'apprécier les connaissances systèmes et des types de données natives (notamment les `dictionaries`).

## Installation
On assume que la gestion de l'environnement est géré par l'utilisateur.

Après avoir récupéré le code source du projet, il faut installer les packages python utilisés :
```
pip install -r requirements.txt 
```

Les scripts des exercices sont prêts à être exécutés.

## Counter
Counter est une application FastAPI minimaliste qui lance un compteur en arrière plan et permet de connaître l'état du compteur via une requête GET.

## Update config file
La description est disponible à `Update_config_file/Exercice - update_config_2_14.md`. L'exercice attend la création d'un script qui aura pour but d'upgrade un fichier de configuration au format YAML en fonction de sa version et de son contenu.

Il est possible de comparer le résultat attendu avec celui obtenu grâce aux fichiers `Update_config_file/default_values/*.yaml` qui contiennent les valeurs attendues.

## Utilisation
### Counter
Voici la commande pour exécuter l'application FastAPI Counter depuis la racine du projet :
```
uvicorn Counter.main:app
```

Il est possible d'ajouter à la commande l'option `--reload` dans le cas où l'utilisateur souhaite modifier le script en parallèle de l'exécution du serveur.

Si l'utilisateur se place dans le répertoire `Counter`, la commande d'exécution sera la suivante :
```
uvicorn main:app
```
---
Pour obtenir l'état courant du compteur sur le navigateur, l'utilisateur doit faire une requête GET sur l'endpoint `localhost:8000/count`.

Sinon, l'état du compteur est affiché dans le terminal.

### Update_config_file
Voici la commande pour exécuter le script qui update le fichier de configuration `application-2.14.yaml` depuis la racine du projet :
```
python ./Update_config_file/update_script.py application-2.14.yaml <output file name>.yaml
```

Le script retournera le résultat dans le fichier `<output file name>.yaml`.

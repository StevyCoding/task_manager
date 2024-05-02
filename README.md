# Documentation du fonctionnement de task_manager.py

Ce script Python est une application de gestion de tâches en ligne de commande. Il permet de stocker, de récupérer, de mettre à jour et de supprimer des tâches dans une base de données PostgreSQL.

## Installation des dépendances

Avant d'exécuter le script, assurez-vous d'avoir installé les dépendances suivantes :
- psycopg2 : un adaptateur PostgreSQL pour Python.
- re : un module Python pour les expressions régulières.

Vous pouvez installer ces dépendances en exécutant la commande suivante :
```bash
pip install psycopg2
```
Utilisation
Pour utiliser le script, exécutez-le à l'aide de Python avec les arguments appropriés depuis la ligne de commande. Voici les différentes commandes disponibles :

- add : Ajoute une nouvelle tâche à la base de données. Vous devrez fournir une description et un statut pour la nouvelle tâche.
- selectAll : Récupère toutes les tâches de la base de données et les affiche.
- update : Met à jour une tâche existante dans la base de données. Vous devrez fournir l'ID de la tâche à mettre à jour, ainsi que la nouvelle description et le nouveau statut.
- delete : Supprime une tâche de la base de données. Vous devrez fournir l'ID de la tâche à supprimer.

Voici un exemple d'utilisation :


```cmd
python task_manager.py add
Description de la tâche : Faire les courses
Statut de la tâche (En cours/En attente/Terminé) : En cours
```

resultat pylint :
```bash
pylint task_manager.py
************* Module task_manager
task_manager.py:31:0: C0301: Line too long (123/100) (line-too-long)
task_manager.py:52:0: C0301: Line too long (103/100) (line-too-long)
task_manager.py:95:0: C0305: Trailing newlines (trailing-newlines)
task_manager.py:1:0: C0114: Missing module docstring (missing-module-docstring)
task_manager.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)
task_manager.py:13:0: C0115: Missing class docstring (missing-class-docstring)
task_manager.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
task_manager.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
task_manager.py:36:4: C0116: Missing function or method docstring (missing-function-docstring)
task_manager.py:47:4: C0116: Missing function or method docstring (missing-function-docstring)
task_manager.py:52:4: C0116: Missing function or method docstring (missing-function-docstring)
task_manager.py:61:4: C0116: Missing function or method docstring (missing-function-docstring)
task_manager.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.94/10 (previous run: 7.62/10, +0.32)
```


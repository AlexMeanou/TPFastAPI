# TPFastAPI

## Initialisation

Afin d'exécuter notre code, nous vous recommandons d'utiliser un environnement virtuel 

        python3 -m venv venv
        source venv/bin/activate

Ensuite vous devrez installer les différentes bibliotèques nécessaires : 
      
        pip install pandas
        pip install tqdm 
        pip install sklearn

Maintenant il va vous falloir préparer un fichier de données, pour ça il vous suffira de lancer le code présent sur le fichier creationFichierCSV.py via la commande suivante :

        python3 creationFichierCSV.py

Il vous est possible de modifier combien de ligne de données vous souhaitez générer, simplement se référer au fichier creationFichierCSV.py et se référer aux commentaires 

## Utilisation 

Sur un terminal à la racine du projet, tapez la commande suivante afin de lancer l'API : 
    
        uvicorn endpoints:app --reload

Maintenant vous pouvez vous rendre à l'adresse suivante : http://localhost:8000/docs et tester les différentes fonctions qui sont disponibles.

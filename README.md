# TPFastAPI

## Initialisation

Afin d'exécuter notre code, nous vous recommandons d'utiliser un environnement virtuel 

        python3 -m venv venv
        source venv/bin/activate

Ensuite vous devrez installer les différentes bibliotèques nécessaires : 
      
        pip install pandas
        pip install tqdm 
        pip install sklearn

## Utilisation 

Sur un terminal à la racine du projet, tapez la commande suivante afin de lancer l'API : 
    
        uvicorn endpoints:app --reload

Maintenant vous pouvez vous rendre à l'adresse suivante : http://localhost:8000/docs et tester les différentes fonctions qui sont disponibles.

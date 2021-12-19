# IMPORT DES LIBRAIRIES
import pandas as pd
import random
from tqdm import tqdm, tqdm_notebook
import sys

# On génère 200 combinaisons perdantes, il faudra en mettre plus si on veut un résultat plus précis
numberOfLosingRows = 200

df_data = pd.read_csv('./euromillions.csv', sep=";")

# Ouverture du fichier
allPossibilitiesFile = open('./EuroMillions_numbers.csv', 'r')

# On récupère toutes les possibilités de combinaisons Euromillions possibles
allPossibilities = allPossibilitiesFile.readlines()

# On récupère leur nombre/taille
maxPossibilities = len(allPossibilities)

#Fermeture du fichier
allPossibilitiesFile.close()

finalFile = open('./euromillions_' + str(numberOfLosingRows+1) + '.csv', 'a')
finalFile.write("Date;N1;N2;N3;N4;N5;E1;E2;Winner;Gain;Result\n")

# On crée pour chaque ligne une combinaison perdante et on la sauvegarde dans le fichier
for index, row in tqdm(df_data.iterrows(), total=len(df_data)):
    rowString = str(row['N1']) + ';' + str(row['N2']) + ';' + str(row['N3']) + ';' + str(row['N4']) + ';' + str(row['N5']) + ';' + str(row['E1']) + ';' + str(row['E2'])
    finalFile.write(row['Date'] + ';' + rowString + ';' + str(row['Winner']) + ';' + str(row['Gain']) + ';win\n')
    generations = []
    for i in range(numberOfLosingRows):

        # On génère une liste de nombres aléatoires
        randomNumber = random.randint(0, maxPossibilities-1)
        randomList = allPossibilities[randomNumber][:-1]

        # On regarde si cette génération est différente de la ligne actuelle (donc si elle est bien perdante)
        while (randomList == rowString or randomNumber in generations):
            randomNumber = random.randint(0, maxPossibilities-1)
            randomList = allPossibilities[randomNumber][:-1]
        generations.append(randomNumber)
        # On l'ajoute au fichier
        finalFile.write(row['Date'] + ";" + randomList + ";0;0;lose" + '\n')
finalFile.close()
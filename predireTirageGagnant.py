# IMPORT DES LIBRAIRIES
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import random
import joblib

def predireTirageProbaGagnant(n1: int, n2: int, n3: int, n4: int, n5: int, e1: int, e2: int):

	# IMPORT CSV
	# Import du csv regénéré avec des combinaisons perdantes, étant donné que le fichier d'origine était composé que de combinaisons gagnantes.
	numberOfLosingRows = 200
	df_data = pd.read_csv('./euromillions_' + str(numberOfLosingRows+1) + '.csv', sep=";")

	# SPLIT DU DATASET
	# On split df_data en Train et Test (90% Train, 10% Test)
	dfTrain = df_data[:int(len(df_data) * 0.90)]
	dtTest = df_data[int(len(df_data) * 0.90):]
	# print(dfTrain.shape, dtTest.shape)

	# On crée un model RandomForest avec sklearn
	model = RandomForestClassifier(n_estimators=1000, random_state=0, verbose=2)

	# On fit le model avec notre data
	model.fit(dfTrain[['N1', 'N2', 'N3', 'N4', 'N5', 'E1', 'E2']].values, dfTrain['Result'].values)

	joblib.dump(model, "./random_forest.joblib")

	# On affiche les résultats du modèle
	print(model.score(dtTest[['N1', 'N2', 'N3', 'N4', 'N5', 'E1', 'E2']].values, dtTest['Result'].values))

	# On génère notre combinaison test (5 nombres entre 1 et 50 & deux nombres entre 1 et 12)
	# set = sorted(random.sample(range(1, 51), 5)).__add__(sorted(random.sample(range(1, 13), 2)))
	# print(set)

	set = []
	set.append(n1)
	set.append(n2)
	set.append(n3)
	set.append(n4)
	set.append(n5)
	set.append(e1)
	set.append(e2)

	# On applique le modèle à notre combinaison test
	result = model.predict_proba([set])
	# Affichage des résultats
	# print(result)
	# print(result[0][1])
	
	# Affichage de la probabilité de gagner	
	return result[0][1]

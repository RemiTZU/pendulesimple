import csv
import os

print("Répertoire de travail:", os.getcwd())


with open('data.csv', 'w', newline='') as fichier:
    writer = csv.writer(fichier)
    writer.writerow([1, 2])
IMAGE_SIZE = 64 # Dimension des images en entrée du réseau
CELL_PER_DIM = 8 # Nombre de cellules en largeur et en hauteur
BOX_PER_CELL = 1 # Nombre d'objets par cellule
NB_CLASSES = 6 # Nombre de classes du problème
PIX_PER_CELL = round(IMAGE_SIZE/CELL_PER_DIM)

CLASS_LABELS = ['danger', 'ordre', 'indication', 'direction', 'localisation', 'complement']

import numpy as np

import math


import PIL
from PIL import Image
import glob, os, sys

for file in glob.glob("*.txt"):
    print(file)

def load_data_detection(ds_path):

    y_paths = []
    # Détermination du nombre d'images total
    for c in CLASS_LABELS:
        path = ds_path + c + '/'
        for file in os.listdir(path):
            if file.endswith('.txt'):
                y_paths.append(os.path.join(path, file))

    dataset_size = len(y_paths)

    # Préparation des structures de données pour x et y
    x = np.zeros((dataset_size, IMAGE_SIZE, IMAGE_SIZE, 3))
    y = []

    for i in range(len(y_paths)):
        text_path = y_paths[i]
        img_path = text_path[:-3] + 'jpg'

        if not os.path.exists(img_path):
            img_path = text_path[:-3] + 'JPG'

        # Lecture de l'image : on va remplir la variable x
        # Lecture de l'image
        img = Image.open(img_path)
        # Mise à l'échelle de l'image
        img = img.resize((IMAGE_SIZE, IMAGE_SIZE), Image.Resampling.LANCZOS)
        # Remplissage de la variable x
        x[i] = np.asarray(img, dtype=np.int32)

        # Texte : coordonnées de boîtes englobantes pour remplir y
        boxes = []
        # Texte : coordonnées de boîtes englobantes pour remplir y
        text_file = open(text_path, "r")
        # Récupération des lignes du fichier texte
        rows = text_file.read().split('\n')
        # Parcours de chaque ligne
        for row in rows:
            if row != '':
                # Séparation des différentes informations
                row = list(row.split(' '))
                box = []
                # réorganisation : les 4 coordonnées de boîte englobantes (castées en flottants) d'abord
                for r in row[1:]:
                    box.append(float(r))

                box_normal = [box[0]-box[2]/2, box[1]-box[3]/2, box[0]+box[2]/2, box[1]+box[3]/2]

                # Puis le label de classe (casté en entier) à la suite
                box.append(int(row[0]))
                boxes.append(box)

        y.append(boxes)
    return x, y

# Chemin vers la base de données
ds_path = "./wildlife/"
x ,y = load_data_detection(ds_path)

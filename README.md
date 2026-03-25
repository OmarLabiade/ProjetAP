# Projet Détection de Panneaux Routiers

## Description
Objectif : détecter 6 types de panneaux routiers à partir d’images.

## Classes
- danger 
- ordre 
- indication 
- direction 
- localisation
- complement

## Dataset
- 500+ images [val : 81; test : 81 ; train : 381] + augmentation sur le data du training(avec roboflow) = 1300+ images [[val : 81; test : 81 ; train : 1143]]
- Sources : photos prises par le groupe (100), captures Google Street View / Google Earth (200), datasets publics Roboflow (200), et images libres de droits (Wikipédia Creative Commons, Getty Images, 43 images).
- Annotation : bounding boxes (format YOLO) outil : https://www.roboflow.com

## Structure

    dataset/
        train/
        val/
        test/
        data.yaml
    README.md

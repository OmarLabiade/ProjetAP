# Projet Détection de Panneaux Routiers

## Description
Objectif : détecter 5 types de panneaux routiers à partir d’images.

## Classes
- danger 
- ordre 
- indication 
- direction 
- localisation
- complement

## Dataset
- 500+ images [val : 81; test : 81 ; train : 381] (5 étudiants) + augmentations sur le data du training(avec roboflow) = 1300+ images [[val : 81; test : 81 ; train : 1143]]
- Sources : photos + images libres de droit (google earth(200), pris (100), data roboflow existantes (200),autres : wikipedia creative commons,gettyimages : 43  )
- Annotation : bounding boxes (format YOLO) outil : https://www.makesense.ai/

## Structure

    dataset/
        train/
        val/
        test/
        data.yaml
    README.md

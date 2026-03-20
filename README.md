# Projet Détection de Panneaux Routiers

## Description
Objectif : détecter 5 types de panneaux routiers à partir d’images.

## Classes
- danger 
- ordre 
- indication 
- direction 
- localisation

## Dataset
- 500 images (5 étudiants)
- Sources : photos + + images libres de droit
- Annotation : bounding boxes (format YOLO) outil : https://www.makesense.ai/

## Structure

    dataset/
        images/
            train/
            val/
            test/
        labels/
            train/
            val/
            test/
        data.yaml
    README.md
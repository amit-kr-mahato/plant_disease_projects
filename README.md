# DataScience_in_project_plant_diseaes_detection
Plant Disease Detection
Overview

This project implements a Plant Disease Detection System using traditional image processing techniques and Python libraries such as NumPy, Pandas, Matplotlib, and OpenCV. The system can identify common diseases in plant leaves from images, helping farmers and gardeners monitor plant health efficiently without needing complex deep learning models.

Features

Detects and highlights diseased areas on plant leaves.

Supports multiple plant types and common leaf diseases.

Visualizes images, histograms, and disease-affected regions using Matplotlib.

Handles datasets efficiently with Pandas for preprocessing and labeling.

Uses OpenCV for image processing operations such as:

Grayscale conversion

Image thresholding

Contour detection

Color space analysis (HSV)

Calculates disease severity based on affected leaf area.

Technologies Used

Python – Programming language

NumPy – Array operations and numerical computations

Pandas – Data handling and dataset management

Matplotlib – Visualization of images and results

OpenCV – Image processing and feature extraction

Workflow

Data Loading – Images and labels are loaded using Pandas and OpenCV.

Preprocessing – Images are resized, converted to grayscale or HSV, and noise is reduced.

Segmentation – Diseased parts of the leaf are segmented using thresholding and masking.

Feature Extraction – Extract color, texture, and contour features from the leaf.

Visualization – Highlight diseased areas and display results with Matplotlib.

Analysis – Compute disease severity or classification results.

Benefits

Lightweight solution compared to deep learning models.

Easy to integrate into mobile or desktop applications.

Helps farmers detect plant diseases early, reducing crop loss.

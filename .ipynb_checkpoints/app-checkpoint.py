import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# =============================
# CONFIG
# =============================
DATASET_PATH = "dataset"
IMG_SIZE = 128

# =============================
# FEATURE EXTRACTION
# =============================
def extract_features(image):
    """
    Extract color + texture features
    """
    # Resize
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Color histogram
    hist = cv2.calcHist([hsv], [0, 1, 2], None,
                        [8, 8, 8], [0, 180, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()

    # Gray image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Texture (mean + std)
    mean = np.mean(gray)
    std = np.std(gray)

    features = np.hstack([hist, mean, std])
    return features

# =============================
# LOAD DATASET
# =============================
features = []
labels = []

print(" Loading dataset...")

for class_name in os.listdir(DATASET_PATH):
    class_path = os.path.join(DATASET_PATH, class_name)

    if not os.path.isdir(class_path):
        continue

    print(f"Processing: {class_name}")

    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)

        image = cv2.imread(img_path)
        if image is None:
            continue

        feature = extract_features(image)
        features.append(feature)
        labels.append(class_name)

X = np.array(features)
y = np.array(labels)

print("Dataset loaded")
print("Total samples:", X.shape[0])

# =============================
# TRAIN TEST SPLIT
# =============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =============================
# MODEL (KNN)
# =============================
print(" Training model...")
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# =============================
# EVALUATION
# =============================
y_pred = model.predict(X_test)

print("\n Accuracy:", accuracy_score(y_test, y_pred))
print("\n Classification Report:\n")
print(classification_report(y_test, y_pred))

# =============================
# TEST ON SINGLE IMAGE
# =============================
def predict_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

    feature = extract_features(image)
    prediction = model.predict([feature])[0]

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f"Prediction: {prediction}")
    plt.axis("off")
    plt.show()

# =============================
# DEMO (CHANGE IMAGE PATH)
# =============================
test_image_path = "dataset/Apple___Apple_scab/0a59e2e0-badb-4b7c-a7a1.jpg"
predict_image(test_image_path)

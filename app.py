import os
import cv2
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# -----------------------------
# FEATURE EXTRACTION
# -----------------------------
def hist_feature(path):

    img = cv2.imread(path)

    if img is None:
        return np.zeros(512)

    img = cv2.resize(img,(128,128))

    hist = cv2.calcHist(
        [img],
        [0,1,2],
        None,
        [8,8,8],
        [0,256,0,256,0,256]
    )

    return hist.flatten()


# -----------------------------
# LOAD TRAIN DATA
# -----------------------------
train_df = pd.read_csv("train_data.csv")

# remove extra spaces in column names
train_df.columns = train_df.columns.str.strip()

class_means = {}

for label in train_df['label'].unique():

    feats = []

    # FIXED HERE (image_path instead of path)
    for p in train_df[train_df['label'] == label]['image_path']:

        if os.path.exists(p):

            feat = hist_feature(p)
            feats.append(feat)

    if len(feats) > 0:
        class_means[label] = np.mean(feats, axis=0)


# -----------------------------
# PREDICTION
# -----------------------------
def predict_disease(path):

    f = hist_feature(path)

    dists = {
        l: np.linalg.norm(f - m)
        for l, m in class_means.items()
    }

    predicted = min(dists, key=dists.get)

    if predicted.lower() == "healthy":
        return "Healthy", 95
    else:
        return "Unhealthy", 90


# -----------------------------
# ROUTES
# -----------------------------
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():

    if 'file' not in request.files:
        return jsonify({"error":"No file uploaded"})

    file = request.files['file']

    if file.filename == "":
        return jsonify({"error":"No file selected"})

    filename = secure_filename(file.filename)

    path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    file.save(path)

    disease,confidence = predict_disease(path)

    if disease == "Healthy":

        desc = "The leaf is healthy and shows no visible disease symptoms."

        prevention = [
            "Maintain proper watering",
            "Ensure sunlight exposure",
            "Use balanced fertilizer"
        ]

    else:

        desc = "The leaf shows signs of plant disease."

        prevention = [
            "Remove infected leaves",
            "Use fungicide spray",
            "Improve air circulation"
        ]

    return jsonify({
        "disease":disease,
        "description":desc,
        "prevention":prevention,
        "confidence":confidence,
        "image_url":"/static/uploads/"+filename
    })


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
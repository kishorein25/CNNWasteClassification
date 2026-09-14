# Waste Classification App

A deep learning web app that classifies waste images into **Biodegradable** or **Non-Biodegradable** using a custom CNN (Convolutional Neural Network) built with TensorFlow / Keras. Users can either **upload a photo** or **capture one live from their webcam**, and get an instant prediction from a friendly Flask web interface.

![Flask](https://img.shields.io/badge/Framework-Flask-blue)
![TensorFlow](https://img.shields.io/badge/ML-TensorFlow-orange)
![Keras](https://img.shields.io/badge/ML-Keras-red)
![Python](https://img.shields.io/badge/Python-3.10-green)
![Deploy](https://img.shields.io/badge/Deploy-Render-purple)

---

## 🔗 Live Demo

**Deployed URL:** [https://cnnwasteclassification-1.onrender.com/](https://cnnwasteclassification-1.onrender.com/)

---

## ⚠️ Important Note

- ✅ **Local / CLI-based prediction works fine** — running `python app.py` from the terminal gives correct predictions (see example terminal output below).
- ❌ **Prediction does NOT work when deployed** — the model does not return predictions on the deployed Render server (`https://cnnwasteclassification-1.onrender.com/`). The app opens and loads the page, but the prediction feature **fails after deployment on the server**.

Example of a local terminal run (works as expected):

```
(tf_keras) PS D:\Projects\waste_classification_app> python app.py
WARNING:tensorflow:No training configuration found in the save file, so the model was *not* compiled. Compile it manually.
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
1/1 [==============================] - 3s 3s/step
127.0.0.1 - - [14/Sep/2026 10:06:46] "POST /predict_webcam HTTP/1.1" 200 -
1/1 [==============================] - 0s 117ms/step
127.0.0.1 - - [14/Sep/2026 10:06:48] "POST /upload HTTP/1.1" 200 -
```

---

## Features

- 📷 **Image Upload** – predict from any image file (JPG / PNG).
- 🎥 **Live Webcam Prediction** – capture a frame from your camera and classify it instantly.
- 🧠 **CNN Model** – powered by a TensorFlow/Keras model trained for waste recognition.
- 🌐 **Clean Web UI** – simple, mobile-friendly Flask frontend.

---

## Tech Stack

| Layer      | Technology                              |
|------------|-----------------------------------------|
| Backend    | Python 3.10, Flask                      |
| Machine Learning | TensorFlow 2.12, Keras, NumPy     |
| Image Processing | OpenCV, Pillow                    |
| Frontend   | HTML, CSS, JavaScript (Webcam API)      |
| Deployment | Render (gunicorn)                       |

---

## Folder Structure

```
waste_classification_app/
│
├── app.py                  # Flask backend: routes, model loading & prediction logic
├── requirements.txt        # Python dependencies
├── .gitignore              # Files/folders excluded from Git
├── .python-version         # Recommended Python version (3.10)
├── README.md               # This file
│
├── model/
│   ├── keras_model.h5      # Trained CNN model (TensorFlow/Keras format)
│   └── labels.txt          # Class labels used during training (Class 1, Class 2)
│
├── templates/
│   └── index.html          # Main page (upload form + webcam capture UI)
│
├── statics/
│   └── style.css           # Stylesheet for the app
│
├── uploads/                # Folder where uploaded images are saved (git-ignored)
│
└── .vscode/
    └── launch.json         # VS Code debug configuration
```

> **Note:** Local Python environments (`venv/`, `tf_keras/`, `tf_old/`) are git-ignored and should **not** be committed.

---

## Prerequisites

Before getting started, make sure you have installed:

- **Python 3.10** – recommended version for TensorFlow 2.12. Download from [python.org](https://www.python.org/downloads/).
- **Git** – [git-scm.com](https://git-scm.com/)
- A webcam (optional, only needed for live webcam predictions).

> On Windows, make sure **"Add Python to PATH"** is checked during installation.

---

## Getting Started (Clone to Run)

Follow these steps to run the project locally on your machine.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/waste_classification_app.git
cd waste_classification_app
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

Your terminal prompt should now show `(venv)`.

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> TensorFlow is a large package, so the installation may take a few minutes.

### 4. Run the app

```bash
python app.py
```

You should see output similar to:

```
 * Running on http://127.0.0.1:5000
```

Open your browser and visit: **http://127.0.0.1:5000**

---

## Usage

1. **Upload an image** – click *Choose File*, select an image of waste (e.g., a plastic bottle, paper, food waste), and press **Predict**.
2. **Webcam prediction** – allow camera access, point it at an object, and click **Capture & Predict**.
3. The app will display the result: **Biodegradable** or **Non-Biodegradable**.

---

## How It Works

1. **Model loading** – The app loads the pre-trained CNN (`model/keras_model.h5`) once at startup (`app.py`).
2. **Preprocessing** – Every input image is resized to **224 × 224 pixels** and normalized to a 0–1 range.
3. **Prediction** – The model outputs a probability score for each class:
   - Class 1 → **Biodegradable**
   - Class 2 → **Non-Biodegradable**
4. **Response** – The result is rendered back on the page via Flask templates.

The model is compatible with a **Google Teachable Machine** exported Keras model (it maps directly to the same input shape and class count).

---

## Deployment (Render)

This project is ready to deploy on [Render](https://render.com):

1. Push the repository to GitHub.
2. In Render, create a **New Web Service** and connect the repo.
3. The build will install dependencies from `requirements.txt` and start with **gunicorn** (included in requirements).
4. Start command (set in Render if prompted):

   ```bash
   gunicorn app:app
   ```

> Set the Python runtime to **3.10** in the Render service settings for best TensorFlow compatibility.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is for educational purposes. If you plan to use it commercially, make sure the model and dataset used for training are properly licensed.
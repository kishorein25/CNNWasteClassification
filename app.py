from flask import Flask, render_template, request, redirect
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import cv2
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Load your Teachable Machine model
model = tf.keras.models.load_model('model/keras_model.h5')

# Class mapping
class_names = {1: "biodegradable", 2: "non-biodegradable"}

# Preprocessing function for uploaded images
def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

# Preprocessing function for webcam frames
def prepare_frame(frame):
    img = cv2.resize(frame, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    return img

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Upload image prediction
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    img = prepare_image(path)
    prediction = model.predict(img)
    class_index = np.argmax(prediction) + 1
    result = class_names[class_index]
    return render_template('index.html', upload_result=result)

# Webcam prediction
@app.route('/predict_webcam', methods=['POST'])
def predict_webcam():
    data_url = request.form['image']
    encoded_data = data_url.split(',')[1]
    decoded_data = base64.b64decode(encoded_data)
    nparr = np.frombuffer(decoded_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = prepare_frame(frame)
    prediction = model.predict(img)
    class_index = np.argmax(prediction) + 1
    result = class_names[class_index]
    return render_template('index.html', webcam_result=result)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)

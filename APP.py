from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load trained model
model = tf.keras.models.load_model('digit_model.h5')

# Create uploads folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_path = None

    if request.method == 'POST':
        file = request.files['file']

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Read image
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

            # Resize image to 28x28
            img = cv2.resize(img, (28, 28))

            # Invert colors
            img = 255 - img
            # Normalize
            img = img / 255.0

            # Reshape for prediction
            img = img.reshape(1, 28, 28)

            # Predict
            pred = model.predict(img)
            prediction = np.argmax(pred)

            image_path = filepath

    return render_template('index.html', prediction=prediction, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)

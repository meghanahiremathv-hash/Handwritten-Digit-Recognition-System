# Handwritten Digit Recognition System

## Overview

This project is a Handwritten Digit Recognition System built using TensorFlow, Keras, OpenCV, and Flask. The application can recognize handwritten digits (0–9) from uploaded images using a neural network trained on the MNIST dataset.

## Features

* Train a digit recognition model using the MNIST dataset.
* Save the trained model as `digit_model.h5`.
* Upload handwritten digit images through a Flask web interface.
* Predict and display the recognized digit.
* Simple and user-friendly interface.

## Technologies Used

* Python
* TensorFlow / Keras
* Flask
* OpenCV
* NumPy
* HTML

## Project Structure

```text
DigitRecognition/
│
├── app.py
├── train_model.py
├── digit_model.h5
│
├── templates/
│   └── index.html
│
├── static/
│   └── uploads/
│
└── README.md
```

## Dataset

The model is trained using the MNIST dataset, which contains 70,000 grayscale images of handwritten digits (0–9).

## Model Training

### Steps

1. Load the MNIST dataset.
2. Normalize image pixel values.
3. Build a neural network using Keras.
4. Train the model.
5. Save the trained model.

### Run Training Script

```bash
python train_model.py
```

After training, the model file `digit_model.h5` will be generated.

## Flask Web Application

### Steps

1. Start the Flask server.
2. Open the application in a web browser.
3. Upload an image containing a handwritten digit.
4. View the predicted digit.

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd DigitRecognition
```

### Install Dependencies

```bash
pip install flask tensorflow numpy opencv-python
```

## Sample Workflow

1. Train the model using `train_model.py`.
2. Verify that `digit_model.h5` is created.
3. Run the Flask application.
4. Upload a handwritten digit image.
5. View the prediction result.

## Future Enhancements

* Support real-time digit drawing on a canvas.
* Improve model accuracy using Convolutional Neural Networks (CNNs).
* Deploy the application to cloud platforms.
* Add confidence scores for predictions.

## Author

Meghana V.H

## License

This project is intended for educational and learning purposes.

from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from PIL import Image

app = Flask(__name__)

#load the trained model
model = tf.keras.models.load_model("mobilenetmodel.h5")
# model.save("snake_classification_model_v2.h5")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
# def predict():
#     file = request.files["file"]
#     image = Image.open(file)
#     image = np.array(image.resize((224, 224))) / 255.0 # preprocessing image

def predict_image_class():
    if "file" not in request.files:
        return "No file uploaded", 400
    
    file = request.files["file"]

    # Check if file is an image
    if file.filename == '':
        return "No file selected", 400
    if not file.filename.lower().endswith(('.webp','.png', '.jpg', '.jpeg')):
        return "Invalid file type. Only WEBP, PNG, JPG, and JPEG files are supported", 400

    try:
        image = Image.open(file)
        image = np.array(image.resize((224, 224))) / 255.0 # preprocessing image

        img_array = np.expand_dims(image, axis=0)

        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])

        if predicted_class == 1:
            result = 'venomous'
        else:
            result = 'non-venomous'
        
        return render_template("result.html", result=result)

    except Exception as e:
        return f"Error processing image: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
# Snake Classification AI

## Overview
Snake Classification AI is a machine learning project designed to classify snakes as either venomous or non-venomous using image analysis. The model is trained using TensorFlow and Keras, and is wrapped in a simple web application for user interaction. This project is intended for educational and recreational purposes.

## Features
- Trained ML model for snake classification (venomous vs non-venomous)
- Built with TensorFlow and Keras libraries
- Interactive web frontend with image upload and prediction functionality
- User-friendly interface for submitting images and viewing classification results
- Error handling for invalid or unsupported image file types

## Setup Instructions

### Prerequisites
- Python 3.x
- TensorFlow
- Keras
- Flask
- Pillow (PIL)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/adhikari-pratik/snake_classification_AI.git
   cd snake_classification_AI
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install packages manually: `pip install flask tensorflow keras pillow`)*

3. Ensure the trained model file (`mobilenetmodel.h5`) is present in the project root.

### Running the Application
```bash
python app.py
```
Open a browser and navigate to `http://localhost:5000` to access the web interface.

### Usage
- Upload an image of a snake.
- Click "Predict" to see whether the snake is classified as venomous or non-venomous.

## Project Structure
- `app.py` – Flask web server and ML inference logic
- `templates/` – HTML templates for web UI
- `static/` – CSS and JavaScript for styling and interactivity
- `mobilenetmodel.h5` – Pre-trained TensorFlow/Keras model

## Example UI
- Upload image button
- Display of uploaded image
- Predict button for classification
- Result page showing the prediction

## License
This project is developed for learning and recreation. Please credit the author if you reuse code.

## Author
[@adhikari-pratik](https://github.com/adhikari-pratik)

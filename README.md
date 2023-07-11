# QR Code Detection and Decoding App

This project is a Python-based application that utilizes YOLOv8 as the underlying model to detect and decode QR codes. The app is built from scratch, and it includes a machine learning pipeline for training the model using a custom dataset generated and preprocessed with Roboflow.

## Installation

To set up the project, follow the steps below:

1. Create a virtual environment to isolate the project dependencies.

```shell
python -m venv env
```

2. Activate the virtual environment
- For Windows:
```shell
env\Scripts\activate
```

- For Linux/macOS:
```shell
source env/bin/activate
```
3. Install the required Python packages by running the following command:
```shell
pip install -r requirements.txt
```

## Model Training
The training of the YOLOv8 model using the custom dataset is documented in the `training_model.ipynb` Jupyter Notebook. The notebook covers the following steps:

- Importing necessary libraries
- Collection and labeling of custom dataset
- Data preprocessing and augmentation using Roboflow
- Splitting the data into training and validation sets
- Training the YOLOv8 model with the custom dataset
- Evaluating the trained model's performance
- Testing the model with new images
- Decoding QR codes from the detected regions

## Running the App
To run the app, follow the instructions below:

1. Change the directory to `dataset/app`:
```shell
cd dataset/app
```

2. Execute the `index.py` file:
```shell
python index.py
```

3. Use http://127.0.0.1:5000 link to use app

![image](https://github.com/rodrigo121998/qr_scanner_scratch/assets/66456730/07bf3c33-43d9-401d-a975-2d3f49452ee1)


The app is built using Flask. The frontend interface can be found in the `templates` folder, specifically in the `index.html` file. The backend logic for QR code detection and decoding is implemented in `main.py` within the `src` folder. The `qr_decode`function, located in `main.py` , performs the required tasks of detecting and decoding QR codes.

Feel free to explore the app, upload images, and see the QR codes being detected and decoded in real time.

**Note**: Ensure that you have the necessary dependencies installed and the trained YOLOv8 model (`yolov8s.pt`) available in the appropriate directory for the app to work correctly.

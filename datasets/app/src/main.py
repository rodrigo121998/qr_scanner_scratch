import cv2
import numpy as np
from flask import jsonify
from ultralytics import YOLO
import os
import base64
from pyzbar.pyzbar import decode as qr_decode
import io
from PIL import Image
import cv2
from .utils import *


def qr_decode(request):
    # Obtener imagen desde el cuerpo de la petición
    image = request.files.get('image').read()
    model = YOLO("../runs/detect/train/weights/best.pt")

    image_yolo = Image.open(io.BytesIO(image))

    results=model.predict(source=image_yolo,conf=0.5)
    #folder_path = '../runs/detect/predict3/crops/QR_CODE' 

    data=[]

    # for i,file in enumerate(os.listdir(folder_path)):
    #     decode_img=cv2.imread(os.path.join(folder_path, file))
    #     if decoder(decode_img)=='No detecta QR':
    #         pass
    #     else:
    #         data.append(decoder(decode_img))

    decode_img=results[0].plot()
    if decoder(decode_img)=='No detecta QR':
        pass
    else:
        data.append(decoder(decode_img))

    if data:
        # Codificar imagen en base64
        image_enc = cv2.imencode('.jpg', decode_img)[1]
        image_enc = base64.b64encode(image_enc).decode()
        # Crear respuesta
        response = {
            'data': str(data),
            'qr_img': str(image_enc),
            'status_code':200
        }
    else:
        response = {
            'data': 'QR no detectado',
            'status_code':404
        }
    return response
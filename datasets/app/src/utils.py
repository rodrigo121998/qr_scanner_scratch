import cv2
from pyzbar.pyzbar import decode as qr_decode

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    try: 
        qr = qr_decode(gray_img)[0]

        qrCodeData = qr.data.decode("utf-8")
        return qrCodeData
    except:
        return "No detecta QR"
from flask import Flask, request, render_template
import cv2
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = ""
    if request.method == 'POST':
        # Get image file from POST request
        image_file = request.files['image']
        image = Image.open(image_file.stream)
        
        # Convert image to numpy array and BGR color format
        img_np = np.array(image)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        
        # QR code detection and decoding
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(frame)
        
        if data:
            return render_template('index.html', data=data)
        else:
            return render_template('index.html', data="QR-Code konnte nicht erkannt werden")
    else:
        return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()

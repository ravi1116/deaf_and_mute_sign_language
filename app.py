from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

# Load Haar cascades
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('cascades/haarcascade_smile.xml')

def decode_image(b64data):
    header, b64 = b64data.split(',', 1)
    img_bytes = base64.b64decode(b64)
    arr = np.frombuffer(img_bytes, np.uint8)
    return cv2.imdecode(arr, cv2.IMREAD_COLOR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_frame', methods=['POST'])
def analyze_frame():
    data = request.json
    frame = decode_image(data['image'])
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    emotion = "Neutral"

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        if len(smiles) > 0:
            emotion = "Happy"
        else:
            emotion = "Neutral"

    response = {
        "emotion": emotion,
        "chatbot_response": chatbot(emotion)
    }
    return jsonify(response)

def chatbot(emotion):
    if emotion == "Happy":
        return "Great to see you smiling! Keep it up 🚀"
    else:
        return "You look a bit neutral. Remember to take a deep breath 🙂"

if __name__ == '__main__':
    app.run(debug=True)

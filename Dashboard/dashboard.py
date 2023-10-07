import cv2
import threading
import numpy as np
from flask import Flask, Response

app = Flask(__name__)

# Create a VideoCapture object for the USB camera (0 is usually the default for the first camera)
camera = cv2.VideoCapture(0)

# Function to generate frames from the camera
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode the frame to JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            # Yield the frame as bytes
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

# Route to display the video feed in a web page
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

import cv2
import threading
import numpy as np
from flask import Flask, render_template, Response

app = Flask(__name__)

# Create a VideoCapture object for the USB camera (0 is usually the default for the first camera)
camera = cv2.VideoCapture(0)

# Function to generate frames from the camera
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode the frame to JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            # Yield the frame as bytes
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

# Main route to render the HTML page
@app.route('/')
def index():
    return render_template('index3.html')

# Route to display the video feed in a web page
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Start the Flask app in a separate thread
    t = threading.Thread(target=app.run, args=('0.0.0.0', 5000))
    t.daemon = True
    t.start()
    app.run(debug=False)

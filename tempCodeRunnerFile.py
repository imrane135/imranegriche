from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve the home page

@app.route('/face-recognition')
def face_recognition():
    return render_template('face_recognition.html')  # Serve the face recognition page

if __name__ == '__main__':
    app.run(debug=True)
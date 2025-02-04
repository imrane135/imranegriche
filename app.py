from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve the home page

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/face-attendance-system/')
def face_attendance_system():
    return render_template('face_attendance_system.html')

@app.route('/projects/dermatological-disease-detection/')
def dermatological_disease_detection():
    return render_template('dermatological_disease_detection.html')

@app.route('/projects/tifinagh/')
def tifinagh_character_recognition():
    return render_template('tifinagh_character_recognition.html')

if __name__ == '__main__':
    app.run(debug=True)

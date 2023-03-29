from flask import Flask, render_template, request, redirect, url_for, session , send_file
from werkzeug.utils import secure_filename
import subprocess
import os 
import cv2
from PIL import Image
import cv2
import re
from detect import recognize_text
import requests
import json
import io
import wave

app = Flask(__name__)
app.config['SECRET_KEY'] = 'magicmagicmagic'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
os.makedirs(os.path.join(static_folder, 'uploads'), exist_ok=True)


@app.route('/')
def index():
    return render_template('indexi.html')



@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file_path = os.path.join(static_folder, 'uploads', filename)
    file.save(file_path)
    session['image_path'] = file_path
    return redirect(url_for('detect_view'))


@app.route('/detect')
def detect_view():
    image_path = session.get('image_path')
    if not image_path:
        return redirect(url_for('upload_view'))

    audio_file, text_result, image_url = detect(image_path)
    return render_template('index.html', audio_file=audio_file, text_result=text_result , image_url = image_url)



def detect(image_path):
    filename = os.path.basename(image_path)
    session['image_filename'] = filename  

    cmd = f"python detect.py --weights best.pt --source {image_path} --save-crop"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, _ = p.communicate()

    text_list = []
    text = recognize_text(f'./runs/detect/web_test2.png')
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = text.replace(',', '')
    text = text.replace('.', '')
    text_list.append(text)

    numbers = re.findall('\d+', text_list[0])
    day = ['년', '월 분 고지서 내역 입니다. ', '년', '월', '일까지 ', '원 납부해주셔야 합니다']
    combined = []
    for i in range(len(numbers)):
        combined.append(numbers[i] + day[i])
    result = ' '.join(combined)
    text_result = result
    print(text_result)

    url = "http://localhost:8080/synthesize"
    data = {'text': text_result}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    container_name_or_id = 'sori'
    local_file_path = 'C:/Users/student/project/testcam/'
    cmd = f"docker cp {container_name_or_id}:/app/static {local_file_path}"
    subprocess.call(cmd, shell=True)

    image_file_path = image_path
    image_url = f"http://127.0.0.1:5000/static/uploads/{filename}"
    print(image_url)
    return ('./static/audio.wav', text_result, image_url)






if __name__ == '__main__':
     app.run(debug=True)
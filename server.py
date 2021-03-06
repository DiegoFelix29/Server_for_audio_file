import main_audio
from flask import Flask
from flask import Response, jsonify, request, redirect, url_for
from flask import render_template, flash, redirect, url_for
from flask import send_from_directory
import shelve
import socket
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './audio'
ALLOWED_EXTENSIONS = set(['wav', 'ogg', 'mp3'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
    print 'upload file'
    try:
       
        os.stat(app.config['UPLOAD_FOLDER'])
    except:        
        os.mkdir(app.config['UPLOAD_FOLDER'])

    if request.method == 'POST':
        file = request.files['file1']
        print 'filename: ' + file.filename

        if file and allowed_file(file.filename):
            print 'allowing file'

            paths=os.path.join(app.config['UPLOAD_FOLDER'])
            filenames = secure_filename(file.filename)
            main_audio.audio(file,paths,filenames)

if __name__ == '__main__':

    app.run(host='0.0.0.0')

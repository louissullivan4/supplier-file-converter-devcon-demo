from flask import Flask, json, request, jsonify, send_file
import os
import urllib.request
from werkzeug.utils import secure_filename
from converter import convert
 
app = Flask(__name__)
  
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['xlsx'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/')
def index():
    return ''

    
@app.route('/upload', methods=['POST'])
def upload():
    if len(os.listdir(app.config['UPLOAD_FOLDER'])) > 0:
        os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], "input.xlsx"))
    elif len(os.listdir(app.config['OUTPUT_FOLDER'])) > 0:
        os.unlink(os.path.join(app.config['OUTPUT_FOLDER'], "output.xlsx"))
    files = request.files.getlist('file')
    if len(files) <= 0:
        resp = jsonify({'message' : 'No file in the request'})
        resp.status_code = 400
        return resp
    if len(files) > 1:
        resp = jsonify({'message' : 'Too many files in the request'})
        resp.status_code = 400
        return resp
    errors = {}
    success = False
    for file in files:
        if file and allowed_file(file.filename):
            file.filename = "input.xlsx"
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'
 
    if success:
        convert(os.path.join(app.config['UPLOAD_FOLDER'], "input.xlsx"))
        resp = jsonify({'message' : 'File succesfully converted'})
        resp.status_code = 201
        # return send_file(os.path.join(app.config['OUTPUT_FOLDER'], "output.xlsx"), mimetype='multipart/form-data')
        return send_file("static/output/output.xlsx", mimetype='multipart/form-data')
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
 
if __name__ == '__main__':
    app.run(debug=True)

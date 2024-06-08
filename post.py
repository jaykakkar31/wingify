from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from sendEmail import send_email
from pdf import file_reader
from crew import crew_main
app = Flask(__name__)
import re
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['pdf']
    receiver_email=''
    try:
        receiver_email = request.form['email']
    except Exception as e:
        print(e)
    if not receiver_email:
        return jsonify({'error': 'No email provided'}), 400
    if not validate_email(receiver_email):
        return jsonify({'error': 'Invalid email address'}), 400
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_dir = 'uploads'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        try:
            file.save(os.path.join(upload_dir, filename))
        except Exception as e:
            print(e)
        file_data = file_reader('./uploads/'+filename)
        try:
            crew_main(file_data,receiver_email)
            return jsonify({'message': 'File uploaded successfully'}), 200
        except Exception as e:
            print(e)
            return jsonify({'error': 'Error processing file'}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == 'pdf'

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    return False

if __name__ == '__main__':
    app.run(port=8000, debug=True)

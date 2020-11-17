from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

import os
from glob import glob

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', filename=filename)
        else:
            return redirect(request.url)
    else:
        for path in glob(os.path.join(app.config['UPLOAD_FOLDER'], '*')):
            os.remove(path)
        return render_template('index.html')


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=os.path.join('uploads', filename)), code=301)


if __name__ == '__main__':
    app.run(debug=True)

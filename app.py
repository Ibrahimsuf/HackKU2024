from flask import Flask, render_template, request
from image_manipulation import image_manipulation
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # Save the file to a folder (in this case, 'uploads' within the 'static' folder)
    filename = os.path.join('static/uploads', file.filename)
    file.save(filename)

    output_path = image_manipulation(filename)

    return render_template("show_image.html", image_name=output_path)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
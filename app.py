from flask import Flask, render_template, request

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
    file.save('static/uploads/' + file.filename)

    return 'File uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True, port=3000)
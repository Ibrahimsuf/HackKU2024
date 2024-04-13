from flask import Flask, render_template, request
from image_manipulation import image_manipulation
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import base64


app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///file_storage.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    file_contents = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file part'

    file = request.files['image']

    if file.filename == '':
        return 'No selected file'

    # Read file contents
    file_contents = file.read()

    # Save file to the database
    new_file = File(filename=file.filename, file_contents=file_contents)
    session.add(new_file)
    session.commit()

    output_img = image_manipulation(new_file, request.form['time'], request.form['Latitude'], request.form['Longitude'])
    img_data = base64.b64encode(output_img.getvalue()).decode()

    return render_template("show_image.html", image_data=img_data)

@app.route("/example")
def example():
  return render_template("example.html")

@app.route("/location", methods=["POST"])
def location():
    longitude = request.form["Longitude"]
    latitude = request.form["Latitude"]
    return f"Longitude: {longitude}, Latitude: {latitude}"

if __name__ == '__main__':
    app.run(debug=True, port=3000)

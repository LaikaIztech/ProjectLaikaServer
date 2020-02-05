from flask import Flask, request
from time import time
from os import remove
from vision.dog_counter import count_doggo

app = Flask(__name__)

@app.route("/", methods=["POST"])
def laika_respond():
    return f"Recognised {request.headers.get('User-Agent')}"

@app.route("/detect", methods=["POST"])
def get_pictures():
    photo_data = request.files['media']
    file_path = f"data/{request.headers.get('User-Agent').replace('/', '')}-{time()}.jpeg"
    photo_data.save(file_path)
    dog_count = count_doggo(file_path, "data/catface.xml")
    print(f"Detected dogs: {dog_count}")
    remove(file_path)
    return f"Dogs in photo: {dog_count}."


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)

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
    photo_data = request.data
    file_path = f"data/{time()}.jpeg"
    with open(file_path, "wb") as file:
        file.write(photo_data)
 #   photo_data.save(file_path)
    #dog_count = count_doggo(file_path, "data/catface.xml")
    #print(f"Detected dogs: {dog_count}")
    #remove(file_path)
    #return f"Dogs in photo: {dog_count}."
    return "Hello."

@app.route("/handshake", methods=["POST"])
def get_handshake():
    print("Handhsake")
    return f"sent handshake request at {time()}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)

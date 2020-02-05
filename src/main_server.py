from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def laika_respond():
    print(request.get_data())
    return f"Recognised {request.headers.get('User-Agent')}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)

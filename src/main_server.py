from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def laika_respond():
    print(request.data)
    return "Request acquired"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)

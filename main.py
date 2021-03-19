from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от гоши теплова"


if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port)

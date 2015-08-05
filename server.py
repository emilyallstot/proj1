from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    testinsta()
    return "<html><body><h1>I am the landing page</h1></body></html>"


if __name__ == "__main__":
    app.run(debug=True)

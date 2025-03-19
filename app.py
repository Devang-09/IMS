import os
from flask import Flask
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, User of IMS!"

app = Flask(__name__, static_folder='images')

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if no PORT env is set
    app.run(host="0.0.0.0", port=port)

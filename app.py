import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Railway!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Get the assigned PORT
    app.run(host="0.0.0.0", port=port)  # Bind to 0.0.0.0

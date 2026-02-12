#!/usr/bin/env python3
import argparse
import os
from flask import Flask, request, send_from_directory, render_template_string

app = Flask(__name__)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>File Upload</title>
</head>
<body>
    <h2>Upload file to remote machine</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <br><br>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_PAGE)

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]

    if file.filename == "":
        return "No selected file", 400

    save_path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(save_path)

    return f"File uploaded successfully: {file.filename}"

@app.route("/uploads/<path:filename>")
def download(filename):
    return send_from_directory(UPLOAD_DIR, filename)

def main():
    parser = argparse.ArgumentParser(description="Simple file upload server")
    parser.add_argument("ip", help="IP address to bind")
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    app.run(host=args.ip, port=args.port)

if __name__ == "__main__":
    main()


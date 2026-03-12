# file_app.py
from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string, flash
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif", "csv"}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.environ.get("FLASK_SECRET", "change-this-secret")

HTML = """
<!doctype html>
<title>Upload / Download</title>
<h2>Upload a file</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file required>
  <button type=submit>Upload</button>
</form>
<p>{{ msg }}</p>
<h3>Available files:</h3>
<ul>
  {% for f in files %}
    <li><a href="{{ url_for('download', filename=f) }}">{{ f }}</a></li>
  {% endfor %}
</ul>
"""

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    msg = ""
    if request.method == "POST":
        if "file" not in request.files:
            msg = "No file part"
        else:
            file = request.files["file"]
            if file.filename == "":
                msg = "No selected file"
            elif allowed_file(file.filename):
                filename = secure_filename(file.filename)
                save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(save_path)
                msg = f"Uploaded {filename}"
            else:
                msg = "File extension not allowed"
    files = sorted(os.listdir(app.config['UPLOAD_FOLDER']))
    return render_template_string(HTML, files=files, msg=msg)

@app.route("/uploads/<path:filename>")
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
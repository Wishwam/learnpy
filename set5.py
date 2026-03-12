# form_app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Process Input</title>
<h2>Enter text to process</h2>
<form method=post>
  <textarea name=text rows=6 cols=60 required></textarea><br>
  <button type=submit>Send</button>
</form>

{% if result %}
  <h3>Result</h3>
  <p><strong>Original:</strong></p>
  <pre>{{ result.original }}</pre>
  <p><strong>Reversed:</strong> {{ result.reversed }}</p>
  <p><strong>Word count:</strong> {{ result.word_count }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def process():
    result = None
    if request.method == "POST":
        text = request.form.get("text", "")
        processed = {
            "original": text,
            "reversed": text[::-1],
            "word_count": len(text.split())
        }
        result = processed
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5004)

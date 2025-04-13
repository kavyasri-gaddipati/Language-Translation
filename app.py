from flask import Flask, render_template, request, jsonify
from translator import translate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.get_json()
    text = data.get("text", "")
    src_lang = data.get("src_lang", "English")
    tgt_lang = data.get("tgt_lang", "Telugu")
    
    try:
        result = translate(text, src_lang, tgt_lang)
        return jsonify({"translation": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

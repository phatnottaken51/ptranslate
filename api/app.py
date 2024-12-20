from flask import Flask, render_template, request, jsonify
from googletrans import Translator
import os

app = Flask(__name__, static_folder='../', template_folder='../templates')
translator = Translator()

# Route phục vụ trang HTML
@app.route('/')
def index():
    return render_template('index.html')

# API để xử lý dịch
@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    source = data.get('source', 'auto')
    target = data.get('target', 'en')

    try:
        translation = translator.translate(text, src=source, dest=target)
        return jsonify({'translated_text': translation.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
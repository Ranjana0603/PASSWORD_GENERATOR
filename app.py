from flask import Flask, request, jsonify, render_template
import random, string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/generate', methods=['GET'])
def generate():
    length = request.args.get('length', default=12, type=int)
    if length < 4 or length > 32:
        return jsonify({"error": "Length must be between 4 and 32"}), 400
    password = generate_password(length)
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
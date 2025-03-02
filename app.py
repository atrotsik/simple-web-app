from flask import Flask, jsonify, send_from_directory
import subprocess

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/script', methods=['GET'])
def run_script():
    try:
        # Исполняем shell-скрипт
        result = subprocess.run(['./script.sh'], capture_output=True, text=True, check=True)
        # Возвращаем результат с HTTP-статусом 200
        return jsonify({"status": "success", "output": result.stdout}), 200
    except subprocess.CalledProcessError as e:
        # В случае ошибки возвращаем HTTP-статус 500
        return jsonify({"status": "error", "output": e.stderr}), 500

@app.route('/script-err', methods=['GET'])
def run_err_script():
    try:
        # Исполняем shell-скрипт
        result = subprocess.run(['./script_err.sh'], capture_output=True, text=True, check=True)
        # Возвращаем результат с HTTP-статусом 200
        return jsonify({"status": "success", "output": result.stdout}), 200
    except subprocess.CalledProcessError as e:
        # В случае ошибки возвращаем HTTP-статус 500
        return jsonify({"status": "error", "output": e.stderr}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

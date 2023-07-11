from flask import Flask, request, jsonify,render_template
from src.main import qr_decode

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/qr_decode', methods=['POST'])
def upload():
    response = qr_decode(request)
    if response["status_code"] == 200:
        return response
    else:
        return response

if __name__ == '__main__':
    app.run(debug=True)
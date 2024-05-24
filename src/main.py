from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello world!'

@app.route('/file', methods=['POST'])
def file():
    file = request.files.get['file']

    return 'File!'
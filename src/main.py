from flask import Flask, request
from src.utils.FileParser import FileParser

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello world!'

@app.route('/file', methods=['POST'])
def file():
    file = request.files.get("file")
    content = file.read()

    parser = FileParser(content)

    return parser.get_raw()
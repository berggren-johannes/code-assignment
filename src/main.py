from flask import Flask, request, Response
from utils.FileParser import FileParser

app = Flask(__name__)

@app.route('/file', methods=['POST'])
def file():
    file = request.files.get("file")
    content = file.read()

    parser = FileParser(content.decode("utf-8"))
    result = ""
    status_code = 200

    try:
        result = parser.get_parsed()
    except ValueError as e:
        result = "Error: " + str(e)
        status_code = 406
    response = Response(response=result, status=status_code)

    return response

if __name__ == '__main__':
    app.run(debug=True, port=8080)
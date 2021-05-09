from flask import Flask
from flask_cors import CORS  


app = Flask(__name__)
CORS(app) 

@app.after_request
def add_header(response):
    # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = "PUT,POST,GET,DELETE,OPTIONS"
    response.headers['Access-Control-Allow-Headers'] = "Content-Type,Content-Length, Authorization"
    return response



if __name__ == "__main__":
    app.run(debug=True)
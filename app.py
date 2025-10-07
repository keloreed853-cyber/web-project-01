from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = os.environ.get('NAME', 'World')
    return f'Hello, {name}!\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


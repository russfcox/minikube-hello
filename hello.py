"""
Basic flask app
"""

from flask import Flask

app = Flask(__name__) # pylint: disable=C0103

@app.route('/')
def home():
    """
    Index route
    """
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
        
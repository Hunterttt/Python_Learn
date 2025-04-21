from flask import Flask
app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return {"message": "Hello world from Flask backend!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
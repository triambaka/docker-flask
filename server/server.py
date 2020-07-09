from flask import Flask
import time
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pore():
    return '<h1>Hello World!</h1>'
    time.sleep(5)
 
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


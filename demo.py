from flask import Flask

app = Flask(__name__)

@app.route('/potato')
def welcome():
    return 'This is first flask '
    #print("HELLO WORLD")

app.run()
from flask import Flask,render_template

# pip install flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'The default route can be shown by slash'

@app.route('/hellopython')
def hellopython():
    return "The append of hello python"



if __name__=='__main__':
    app.run()

# search for anaconda prompt in your system

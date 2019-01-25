from flask import Flask

#Initiate flaskapp 

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello, World'

@app.route('/hello')
def hello_word2():
    return 'Hello, David'

if __name__=="__main__":
    app.run(debug=True)
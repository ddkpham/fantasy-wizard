from flask import Flask
from flask import render_template

#Initiate flaskapp 

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello, World'

@app.route('/render')
def temp_render():
    return render_template('index.html')

@app.route('/scrape')
def web_scrape():
    return 'scraping to be implemented soon!'


if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template
from flask.json import jsonify

app = Flask(__name__)

@app.route('/')
def initialize():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/publications/')
def publications():
    return render_template('publications.html')

@app.route('/news/')
def news():
    return render_template('news.html')

@app.route('/skills/')
def skills():
    return render_template('skills.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

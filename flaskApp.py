from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route('/page1/')
def SanDiego():
    return render_template('maps/SanDiego.html')

@app.route('/page2/')
def LosAngeles():
    return render_template('maps/LA.html')

@app.route('/page3/')
def SanFrancisco():
    return render_template('maps/SF.html')

@app.route('/page4/')
def Portland():
    return render_template('maps/Portland.html')

@app.route('/page5/')
def Seattle():
    return render_template('maps/Seattle.html')

if __name__ == "__main__":
    app.run(debug=True)
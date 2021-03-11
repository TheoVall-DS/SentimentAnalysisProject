from flask import Flask, render_template, request
from model import SentimentClassifier

clf = SentimentClassifier()
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index_page():
    if request.method == 'POST':
        text = request.form['text']
        prediction_message = clf.getSentiment(text)
        return render_template('index.html', text = text,
                               prediction_message = prediction_message)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
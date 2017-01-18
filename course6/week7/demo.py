__author__ = 'astar'
from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)

print "Preparing classifier for sentiment analysis demo"
start_time = time.time()
classifier = SentimentClassifier()
print "Classifier is ready"
print time.time() - start_time, "seconds"

@app.route("/sentiment-demo", methods=["POST", "GET"])
def index_page(text="", prediction_message_pos="", prediction_message_neg=""):    
    if request.method == "POST":
        text = request.form["text"]
        logfile = open("ydf_demo_logs.txt", "a", "utf-8")        
        print >> logfile, text
        prediction = classifier.get_prediction([text])
        prediction_message = classifier.get_prediction_message(prediction)    
        if prediction == 1:
            prediction_message_pos = prediction_message
        else:
            prediction_message_neg = prediction_message
        print >> logfile, prediction_message    
        logfile.close()
    return render_template('sentiment_demo2.html', text=text, prediction_message_pos=prediction_message_pos, prediction_message_neg=prediction_message_neg)    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)

from flask import Flask,render_template,jsonify

app = Flask(__name__)

tmpData = {"title":"loc","data":[{"name":"abc-1234","loc":[{"lng":121.536099,"lat":25.028136},{"lng":121.534426,"lat":25.075181},{"lng":121.558623,"lat":25.038996}]},{"name":"abc-4567","loc":[{"lng":121.546099,"lat":25.028136},{"lng":121.644426,"lat":25.075181},{"lng":121.748623,"lat":25.038996}]}]}

@app.route("/")
def home():
    return jsonify(tmpData)

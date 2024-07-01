from flask import Flask

app = Flask(__name__)
rss_contents = ""

def load_contents():
    global rss_contents
    with open("static/sample_rss.xml", "rt") as fin:
        rss_contents = fin.read()

@app.route("/")
def hello_world():
    load_contents()
    return rss_contents

@app.route("/rss")
def rss():
    load_contents()
    return rss_contents

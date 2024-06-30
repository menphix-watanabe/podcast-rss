from flask import Flask

app = Flask(__name__)
rss_contents = ""

def load_contents():
    global rss_contents
    with open("static/sample_rss.xml", "rt") as fin:
        rss_contents = fin.read()

@app.route("/")
def hello_world():
    return rss_contents

if __name__ == "__main__":
    load_contents()
    app.run(host="0.0.0.0", port=8000, debug=True)
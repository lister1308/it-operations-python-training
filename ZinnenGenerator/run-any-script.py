from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    # macos
    #output = subprocess.check_output(["/opt/homebrew/bin/python3.9", "/Users/lucas/stack/Python/itoperations/ZinnenGenerator/zinnengenerator.py"])
    # windows
    output = subprocess.check_output(["python", "c:\\Users\\tepperl\\Python\\it-operations-python-training\\ZinnenGenerator\\zinnengenerator.py"])
    return output.decode()

app.run(host='0.0.0.0', port=8080)
from flask import Flask, request, render_template
import subprocess
import platform
#from googlesearch import search

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if platform.system() == 'Windows':
        output = subprocess.check_output(["python", "c:\\Users\\tepperl\\Python\\it-operations-python-training\\ZinnenGenerator\\zinnengenerator.py"])
    else:
        output = subprocess.check_output(["/opt/homebrew/bin/python3.9", "/Users/lucas/stack/Python/itoperations/ZinnenGenerator/zinnengenerator.py"])
    # zoek naar afbeeldingen
    """
    zin = output.decode().strip()
    urls = []
    for url in search(zin, num_results=10):
        print(url)
        if url.endswith(('.jpg', '.jpeg', '.png')):
            urls.append(url)
            break

    # print de URL
    #print(urls[0])
    print(urls)
    """
    return output.decode().strip()

app.run(host='0.0.0.0', port=8080)
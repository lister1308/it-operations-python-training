from flask import Flask, request, render_template, jsonify
import subprocess
import platform
from duckduckgo_search import ddg_images

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if platform.system() == 'Windows':
        #output = subprocess.check_output(["python", "c:\\Users\\tepperl\\Python\\it-operations-python-training\\ZinnenGenerator\\zinnengeneratorv2.py","--print","zin","--aantal","1"])
        runscript = ["python", "c:\\Users\\tepperl\\Python\\it-operations-python-training\\ZinnenGenerator\\zinnengeneratorv2.py"]
    else:
        #output = subprocess.check_output(["/opt/homebrew/bin/python3.9", "/Users/lucas/stack/Python/itoperations/ZinnenGenerator/zinnengeneratorv2.py","--print","zin","--aantal",'1'])
        runscript = ["/opt/homebrew/bin/python3.9", "/Users/lucas/stack/Python/itoperations/ZinnenGenerator/zinnengenerator-testlucas.py"]
    # voeg parameters toe
    #zinalinea_type = request.form.get('type', 'zin') # Standaardwaarde is 'zin'

    sound = request.form.get('sound', False) # Standaardwaarde is False
    if sound:
        runscript.append("--sound")

    #coherence = request.form.get('coherence', False) # Standaardwaarde is False

    runscript.extend(["--print","zin","--aantal","1"])
    # run script
    output = subprocess.check_output(runscript)

    # zoek naar afbeeldingen met de zoekopdracht uit 'output'
    results = ddg_images(output.decode().strip())
    # controleer of er afbeeldingsresultaten zijn
    image_url = ''
    if results:
        # haal de URL van de eerste afbeelding op
        image_url = results[0]['image']
    return jsonify({
    "text": output.decode().strip(),
    "image_url": image_url
})

app.run(host='0.0.0.0', port=8080)
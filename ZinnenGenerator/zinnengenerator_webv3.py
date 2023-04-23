from flask import Flask, request, render_template, jsonify
import subprocess
import platform
from duckduckgo_search import ddg_images
from zinnengenerator_dictv3 import docenten

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if platform.system() == 'Windows':
        #runscript = ["python", "c:\\Users\\tepperl\\Python\\it-operations-python-training\\ZinnenGenerator\\zinnengeneratorv3.py"]
        runscript = ["python", "zinnengeneratorv3.py"]
    else:
        #runscript = ["/opt/homebrew/bin/python3.9", "/Users/lucas/stack/Python/itoperations/ZinnenGenerator/zinnengeneratorv3.py"]
        runscript = ["/opt/homebrew/bin/python3.9", "zinnengeneratorv3.py"]
    # process parameters vanuit webpagina
    # print een zin of volledige alinea
    zinalinea_print = request.form.get('print', 'zin') # Standaardwaarde is 'zin'
    runscript.extend(["--print",zinalinea_print])
    # moet de zin worden uitgesproken
    sound = request.form.get('sound', False) # Standaardwaarde is False
    if sound:
        runscript.append("--sound")
    # aantal zinnen
    aantal = request.form.get('aantal','1')
    runscript.extend(['--aantal',aantal])
    # gebruik maken van samenhang
    samenhang = request.form.get('samenhang', False) # Standaardwaarde is False
    if samenhang:
        runscript.append('--samenhang')
    # thema
    thema = request.form.get('thema',None)
    if not thema == None:
        runscript.extend(['--thema',thema])
    # run script
    output = subprocess.check_output(runscript)

    output = output.decode().strip()
    output = str(output)
    #
    # controleer of 1 van de docenten het onderwerp is
    zin = output.split()
    gevonden = False
    for woord in zin:
        if woord in docenten:
            image_url = f"/static/{woord}-foto.png"
            gevonden = True
            break
    if not gevonden:
        # zoek naar afbeeldingen met de zoekopdracht uit 'output'
        results = ddg_images(output)
        # controleer of er afbeeldingsresultaten zijn
        image_url = ''
        if results:
            # haal de URL van de eerste afbeelding op
            image_url = results[0]['image']
        if image_url == '':
            image_url = "/static/cursusburo-logo.png"
    return jsonify({
    "text": output,
    "image_url": image_url
})

app.run(host='0.0.0.0', port=8080)
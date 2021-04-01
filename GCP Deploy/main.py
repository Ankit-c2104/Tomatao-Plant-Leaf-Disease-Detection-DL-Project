from flask import render_template, Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
from Encode_Decode_utils.utils import decodeImage
from predict import plantleaf

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

application = Flask(__name__)
CORS(application)


#class ClientApp():
#    def __init__(self):
#        self.filename = 'InputFilename.jpg'
#        self.classifier = plantleaf(self.filename) # creating a object of plantleaf class


@application.route("/", methods=['GET'])
@cross_origin()
def home():
    if request.method == "GET":
        return render_template('index.html')

@application.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
   if request.method == "POST":
    image_file = request.files['file']
    #print(image_file)
    #decodeImage(image, clApp.filename)
    classifier = plantleaf()  # creating a object of plantleaf class
    result = classifier.predictPlantImage(image_file)
    return result
   else:
       print('Loading Error')


if __name__ == "__main__":
    #clApp = ClientApp()
    application.run(debug=True)
    #application.run(host='0.0.0.0', port=8080, debug=True)



#entrypoint: gunicorn -b :$PORT main:app.server --timeout 120
import numpy as np
import os
from tensorflow import keras
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
# from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import render_template
#pip install pillow
import io
#import cloudstorage as gcs
#from google.appengine.api import app_identity


class plantleaf:
    #def __init__(self, filename):
    #    self.filename = filename

    def predictPlantImage(self, image_file):

        self.image_file = image_file

        # load the model
        model = load_model('PlantLeafCNN_2021-03-18_final_VGG16.h5')
        # model = load_model('PlantLeafCNN_2021-03-04 _Basic_CNN.h5')

        #Save the file to ./uploads

        basepath = os.path.dirname(__file__) # - org
        #basepath = os.path.dirname('Last Try')

        file_path = os.path.join(basepath, 'uploads', secure_filename(self.image_file.filename)) # - org
        # secure_filename - Pass it a filename and it will return a secure version of it.
        # This filename can then safely be stored on a regular file system and passed to os.

        #file_path = os.path.dirname('Last Try/temp')

        self.image_file.save(file_path)  # save the image for further use - org

        test_image = image.load_img(file_path, target_size=(224, 224)) # should be same as given in the code for input
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255
        test_image = np.expand_dims(test_image, axis=0)  # expand dimension - flattening it

        preds = model.predict(test_image)
        #print(preds)

        preds = np.argmax(preds,axis=1)  # The numpy. argmax() function returns indices of the max element of the array in a particular axis.
        #print(preds)

        if preds == 0:
            prediction = "Tomato - Bacterial Spot"
            return prediction
        elif preds == 1:
            prediction = "Tomato - Early Blight"
            return prediction
        elif preds == 2:
            prediction = "Tomato - Late Blight"
            return prediction
        elif preds == 3:
            prediction = "Tomato - Leaf Mold"
            return prediction
        elif preds == 4:
            prediction = "Tomato - Septoria Leaf Spot"
            return prediction
        elif preds == 5:
            prediction = "Tomato - Target Spot"
            return prediction
        elif preds == 6:
            prediction = "Tomato - Yellow Leaf Curl Virus"
            return prediction
        elif preds == 7:
            prediction = "Tomato - Mosiac Virus"
            return prediction
        elif preds == 8:
            prediction = "Tomato - Healthy"
            return prediction
        else:
            prediction = "No Match"
            return prediction
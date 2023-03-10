from flask import Flask, request
from tensorflow import keras
import numpy as np
import pandas as pd


app = Flask(__name__)

model = keras.models.load_model('mnistModel.h5')

class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt',
               'Sneaker','Bag','Ankle boot']

@app.route('/classify', methods=['POST'])
def classify():
    image_data = request.get_json()
    query = pd.DataFrame(image_data)
    query = query/255
    prediction = model.predict(query).tolist()
    print(prediction)

    max = np.argmax(prediction)
    type = class_names[max]

    dic={"Type":type,"values":prediction}
    return dic

if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True)


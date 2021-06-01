#@ Importing Required Libraries
import os 
import streamlit as st
import pandas as pd
import numpy as np 
import tensorflow as tf
from PIL import Image
  
html_temp = """
    <div style="background-color:#0b0975;padding:17px;border-radius:30px">
    <h1 style="color:white;font-weight:bold;text-align:center;">Traffic Sign Classifier</h1>
    <h4 style="color:white;text-align:center">~Made by Nakshatra Singh ❤️</h4>
    </div>  
"""

#@ This markdown line allows us to display the front end aspects we have defined in the code.
#@ By default, any HTML tags found in the body will be escaped and therefore treated as pure text. 
#@ This behavior may be turned off by setting this argument to True. 

st.markdown(html_temp, unsafe_allow_html=True)

st.markdown('#')

#@ loads the saved model into cache using streamlit's "@st.cache" feature
@st.cache(allow_output_mutation=True)

def load_model():
    model=tf.keras.models.load_model('model_traffic_sign.h5')
    return model 

model = load_model()

#@ uploading image
uploaded_file = st.file_uploader("Please upload an image") 

if uploaded_file is None:
    st.text("")

else:
    
    #@ opening image 
    image = Image.open(uploaded_file) 
    
    #@ showing image in a html page
    st.image(image,width=250)
    
    #resizing image
    image = image.resize((30,30))
    
    #converting into array
    image = np.asarray(image)

    image = image[:, :, :3]
    
    #@ model trained for 30*30
    image = np.array(image).reshape(1, 30, 30, 3).astype(float)

    #@ scaling
    image = image/255

    #@ predictions
    pred = np.argmax(model.predict(image), axis=-1)

    def getClassName(classNo):
        if classNo == 0:
            return 'Speed limit 20 km/h'
        elif classNo == 1:
            return 'Speed limit 30 km/h'
        elif classNo == 2:
            return 'Speed limit 50 km/h'
        elif classNo == 3:
            return 'Speed limit 60 km/h'
        elif classNo == 4:
            return 'Speed limit 70 km/h'
        elif classNo == 5:
            return 'Speed limit 80 km/h'
        elif classNo == 6:
            return 'End of speed limit 80 km/h'
        elif classNo == 7:
            return 'Speed limit 100 km/h'
        elif classNo == 8:
            return 'Speed limit 120 km/h'
        elif classNo == 9:
            return 'No passing'
        elif classNo == 10:
            return 'No passing for vechiles over 3.5 metric tons'
        elif classNo == 11:
            return 'Right-of-way at the next intersection'
        elif classNo == 12:
            return 'Priority road'
        elif classNo == 13:
            return 'Yield'
        elif classNo == 14:
            return 'Stop'
        elif classNo == 15:
            return 'No vechiles'
        elif classNo == 16:
            return 'Vechiles over 3.5 metric tons prohibited'
        elif classNo == 17:
            return 'No entry'
        elif classNo == 18:
            return 'General caution'
        elif classNo == 19:
            return 'Dangerous curve to the left'
        elif classNo == 20:
            return 'Dangerous curve to the right'
        elif classNo == 21:
            return 'Double curve'
        elif classNo == 22:
            return 'Bumpy road'
        elif classNo == 23:
            return 'Slippery road'
        elif classNo == 24:
            return 'Road narrows on the right'
        elif classNo == 25:
            return 'Road work'
        elif classNo == 26:
            return 'Traffic signals'
        elif classNo == 27:
            return 'Pedestrians'
        elif classNo == 28:
            return 'Children crossing'
        elif classNo == 29:
            return 'Bicycles crossing'
        elif classNo == 30:
            return 'Beware of ice/snow'
        elif classNo == 31:
            return 'Wild animals crossing'
        elif classNo == 32:
            return 'End of all speed and passing limits'
        elif classNo == 33:
            return 'Turn right ahead'
        elif classNo == 34:
            return 'Turn left ahead'
        elif classNo == 35:
            return 'Ahead only'
        elif classNo == 36:
            return 'Go straight or right'
        elif classNo == 37:
            return 'Go straight or left'
        elif classNo == 38:
            return 'Keep right'
        elif classNo == 39:
            return 'Keep left'
        elif classNo == 40:
            return 'Roundabout mandatory'
        elif classNo == 41:
            return 'End of no passing'
        elif classNo == 42:
            return 'End of no passing by vechiles over 3.5 metric tons'

    st.write("Predicted class ↪ " + str(getClassName(pred[0])))
     
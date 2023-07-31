import numpy as np
import keras
from PIL import Image
import streamlit as st

reconstructed_model = keras.models.load_model("./models/TSignClass.keras")

def get_label_text(int_label):
    dict_labels = {0: 'Speed limit 20km/h', 1: 'Speed limit 30km/h', 2: 'Speed limit 50km/h',  3: 'Speed limit 60km/h',
4: 'Speed limit 70km/h',  5: 'Speed limit 80km/h', 6: 'End of speed limit 80km/h',  7: 'Speed limit 100km/h', 
8: 'Speed limit 120km/h',  9: 'No passing', 10: 'No passing if over 3.5 tons', 11: 'Right-of-way at next intersection', 
12: 'Priority road', 13: 'Yield', 14: 'Stop', 15: 'No vehicles', 16: 'Vehicles over 3.5 tons prohibited', 
17: 'No entry', 18: 'General caution', 19: 'Dangerous curve to the left', 20: 'Dangerous curve to the right', 
21: 'Double curve', 22: 'Bumpy road', 23: 'Slippery road', 24: 'Road narrows on the right', 25: 'Road work', 
26: 'Traffic signals', 27: 'Pedestrians', 28: 'Children crossing', 29: 'Bicycles crossing', 30: 'Beware of ice/snow',
31: 'Wild animals crossing', 32: 'End of speed and passing limits', 33: 'Turn right ahead', 34: 'Turn left ahead', 
35: 'Ahead only', 36: 'Go straight or right', 37: 'Go straight or left', 38: 'Keep right', 39: 'Keep left', 
40: 'Roundabout mandatory', 41: 'End of no passing', 42: 'End of no passing over 3.5 tons'}
    return dict_labels[int_label]

def preprocess_image(img_array):
    img_array = np.reshape(img_array, (1, img_array.shape[0], img_array.shape[1], img_array.shape[2]))

    img_array_gray = np.sum(img_array/3, axis = 3, keepdims=True)

    img_array_gray_norm = (img_array_gray - 128) / 128

    # Convert the NumPy array to a PIL Image
    pil_image = Image.fromarray(np.squeeze(img_array_gray_norm))

    # Define the target size
    target_size = (32, 32)

    # Resize the image using Pillow's resize method
    resized_image = pil_image.resize(target_size, Image.ANTIALIAS)

    # Convert the resized PIL Image back to a NumPy array
    resized_image_array = np.expand_dims(np.array(resized_image), axis=-1)

    resized_image_array = resized_image_array.reshape(1, 32, 32, 1)

    return resized_image_array

def class_page():
    # Add an "Upload Image" widget

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "jfif"])

    if uploaded_image is not None:

        # Display the uploaded image
        st.image(uploaded_image, caption='Uploaded Image')

        img = Image.open(uploaded_image)
        img_array = np.array(img)
            
        img_array = preprocess_image(img_array)

        predict_x = reconstructed_model.predict(img_array)
        predicted_classes = np.argmax(predict_x, axis=1)

        return predicted_classes

    else:
        pass

predicted_classes = class_page()

button_click = st.button('Predict my image:')

if button_click:
    st.text(f'The predicted class for your image is: {predicted_classes[0]}-{get_label_text(predicted_classes[0])}')
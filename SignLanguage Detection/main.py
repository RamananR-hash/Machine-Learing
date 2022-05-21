import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import tkinter
from tkinter import filedialog
import warnings
warnings.filterwarnings("ignore")
import speak

classes = {
0:"TWO",1: "THREE",2: "FOUR",3: "FIVE",4: "SIX",5: "SEVEN",6: "EIGHT",7: "NINE",
8: "A",9: "B",10:"C",11: "D",12: "E",13: "F",14: "G",
15: "H",16: "I",17: "K",18: "L",19: "M",20: "N",21: "O",22: "P",23: "Q",24: "R",
25: "S",26: "T",27: "U",28: "V",29: "W",30: "X",31: "Y",32: "Z",33: "ONE",34: "J"

           }

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5',compile=False)


# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
while True:
    tkinter.Tk().withdraw()
    img_path = filedialog.askopenfilename()

    # Replace this with the path to your image
    image = Image.open(img_path)

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    #image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    #print(prediction)
    max_val = max(prediction[0])
    index = np.where(prediction[0] == max_val)

    output = classes[int(str(index[0])[-2])]
    speak.Speak(output)
    print(output)


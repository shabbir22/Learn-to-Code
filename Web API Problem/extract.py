'''import cv2
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images
folder='C:/DOER/Learn to Code/Data Extraction from NID Image'

'''
import os
import base64

directory = r"C:\DOER\Learn to Code\Data Extraction from NID Image"
files = os.listdir(directory)

image_64_encode=''
for file in files:
    if os.path.isfile(file):
        image = open(file, 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        print(image_64_encode)

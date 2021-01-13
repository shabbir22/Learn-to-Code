#Python Code to Convert JPG to Encoded String Value and Keep it in a list of string:

import os
import base64

words = []
'''
directory = 'E:/pictures'    #directory path where all the images are kept
for filename in os.listdir(directory):
'''

#Look thorugh all the files in the directory
    if filename.endswith(".jpg"):     #Only look for files with extention .jpg
        with open(os.path.join(directory, filename), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            words.extend(encoded_string)
            
    else:
        continue
print(words)

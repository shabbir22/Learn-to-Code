 
import os
import base64

directory = "C:\\DOER\\Learn to Code\\Data Extraction from NID Image"
files = os.listdir(directory)
my_string=''
for file in files:
    if os.path.isfile(file):
        with open(os.path.join(file, 'rb')) as image_file:
            my_string = base64.b64encode(image_file.read())
            print(my_string)


import os
import base64

directory = "C:\\DOER\\Learn to Code\\Data Extraction from NID Image"
files = os.listdir(directory)
image_64_encode=''
for file in files:
    if os.path.isfile(file):
        image=open(os.path.join(file, 'rb'))
        image_read=image.read()
        image_64_encode = base64.encodebytes(image_read)
        print(image_64_encode)




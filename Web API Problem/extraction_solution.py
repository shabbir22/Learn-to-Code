import base64
import os
for file in os.listdir("C:\\Users\shabb\\Desktop\\Data Extraction from NID Image"):
    if file.endswith(".jpg"):
        with open("", "rb") as image_file:
            data = base64.b64encode(image_file.read())
            print(data)

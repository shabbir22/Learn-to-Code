import os
import base64
import requests
import numpy as np

nid_data=[]

url = "http://172.16.7.17:8005/v1/api/nidscan/"
#Read filename and convert nid images to base64 string :
directory = "E:\\Learn to Code\\Web API Problem\\NID Data"
print()
for filename in os.listdir(directory):
    if filename.endswith(".jpg"): 
         with open(os.path.join(directory, filename), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            decoded_string = encoded_string.decode('utf-8')

            print(filename, encoded_string.decode('utf-8'))
            
            #body="{\r\n\"image\": \""+encoded_string.decode('utf-8')+"\"\r\n}"
            body="{\"image\": \""+decoded_string+"\"}"
            headers = {
            'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, data=body)
            print()
            print(filename)
            print()
            print(response.text)
            #get data from txt:
            data = np.genfromtxt(response, skip_header = 4)
            #append data
            nid_data.append(data)

first_source_data = nid_data[0]
            

import os   #Module to read data from local folder
import base64    #Module to convert image into string information
import requests  #Module to requests data from API
import timeit   #To get the program execution time

url = "http://172.16.7.17:8005/v1/api/nidscan/"     #URL for the API

#Read filename and convert nid images to base64 string :

directory = "E:\\Learn to Code\\Web API Problem\\NID Data"   #Directory where NID images are stored

for filename in os.listdir(directory):    #Reading the image files one by one from the local directory
    if filename.endswith(".jpg"):         #Reading the files only with .jpg extension
         with open(os.path.join(directory, filename), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())    #Encoding the image as base64 string
            #file_size=os.path.getsize('filename')
            #image_size_in_base64 = ((len(encoded_string) * 6 - encoded_string.count('=') * 8) / 8)/1000
            #as image size can be calculated from the string length. Since every character represents 6 bits and every '=' sign shows lack of 8 bits.
            decoded_string = encoded_string.decode('utf-8')         #In image string format

            #print(filename, decoded_string)
            
            #body="{\r\n\"image\": \""+encoded_string.decode('utf-8')+"\"\r\n}"

            body="{\"image\": \""+decoded_string+"\"}"      #json body where the decoded string should be passed for NID data extraction
            headers = {
            'Content-Type': 'application/json'
            }
            #start = timeit.default_timer()    ##sending requests time
            
            response = requests.post(url, headers=headers, data=body)    #requesting NID information from API

            #stop = timeit.default_timer()
            #response_time=stop-start        ##Time taken to get the response after sending it
            
            print()
            print(filename)    #printing the image file name
            print()
            print(response.text)   #Printing the NID Data
            with open(filename[0:-4]+'.txt', 'w') as f:      #Creating different file names with different image file names from the directory
               f.write(response.text)                        #Writing the NID information of the Image in the respective file

               #To also add the name of the file and string length
               #f.write (filename[0:-4]+'.txt', response_time, file_size, len(response), os.stat(filename.txt).st_size, image_size_in_base64, response.text)

               
               

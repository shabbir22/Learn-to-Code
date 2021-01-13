#importing modules
import os
import base64
import requests
import sys
import shutil
url = "http://172.16.7.17:8005/v1/api/nidscan/"

directory = 'C:/Users/Mainur/Pictures/example'
#Read one file at a time and convert to base64 string
print("File name with base64 strings and Information:","\n")
for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                with open(os.path.join(directory, filename), "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                    decode_utf = encoded_string.decode('utf-8')
                    print("File Name:",filename,"         base64 String:",decode_utf)
                    body="{\"image\": \""+decode_utf+"\"}"
                    headers = {
                    'Content-Type': 'application/json'
                    }
                    #requesting NID information from API
                    response = requests.post(url, headers=headers, data=body)
                           
                    #print(response.text)
                    #print()
                    #print(filename,"Information:")
                    #print()
                    '''
                    with open(filename[0:-4]+'.txt', 'w') as f:
                        f.write(response.text)
                        '''
                    #Creating different file names with details.
                    original_stdout = sys.stdout
                    file_name = "C:/Users/Mainur/AppData/Local/Programs/Python/Python39/NID"
                    with open(filename[0:-4]+'.txt', 'w') as f:
                            sys.stdout = f # Change the standard output to the file we created.
                            base64_file_size = len(decode_utf) * 3 / 4 - decode_utf.count('=')
                            file_stats = os.stat(file_name)
                            print("File Name: ",filename,"\n",
                                  "NID Information:",(response.text),"\n",
                                  "File Size:",file_stats.st_size/1024,"kb","\n",
                                  "base64 File Size:",base64_file_size/1024,"kb","\n",
                                  "Response Time:",response.elapsed.total_seconds(),"Sec","\n",)
                            sys.stdout = original_stdout
                            # Reset the standard output to its original value



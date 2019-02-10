import os
import requests

path = "./public/"

def validateProject():
    report = {}
    for file in os.listdir(path):
        if file.endswith(".html"):
            file = os.path.join(path, file);
            report[file] = requests.post('https://validator.w3.org/nu/?out=json', files={'upload_file': open(file, 'rb')})
    return report;
        
    
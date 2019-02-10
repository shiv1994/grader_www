from html_validator import validate
import os

path = "./public/"

def validateProject():
    report = {}
    for file in os.listdir(path):
        if file.endswith(".html"):
            file = os.path.join(path, file);
            report[file] = validate(file)
    return report
        
    

import os, json, webbrowser
from html.parser import HTMLParser

class MyParser(HTMLParser):
    start_tags = []
    end_tags = []

    def handle_starttag(self, tag, attrs):
        self.start_tags.append(tag)
    
    def handle_endtag(self, tag):
        self.end_tags.append(tag)
    
    def find_proper_tags(self):
        start_tags = set(self.start_tags)
        end_tags = set(self.end_tags)
        return (start_tags and end_tags)

def determine_os():
    if os.name == 'posix':
        return 'open -a /Applications/Google\ Chrome.app %s'
    elif os.name == 'nt':
        return 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    else:
        return '/usr/bin/google-chrome %s'

def determine_marks():
    # Get current working directory.
    cwd  = os.getcwd()
    # Path to html file.
    html_file_path = cwd + "/scripts/home.html"
    # Load html file that will be checked.
    html_file = open(html_file_path, "r").read()
    # Load json file containing mark scheme.
    with open(cwd + "/tags.json", "r") as json_tags_file:
        html_tag_data = json.load(json_tags_file)
    # Initiate parser and feed file into it.
    parser = MyParser()
    parser.feed(html_file)
    # Determine the tags that have beginning and closing elements.
    proper_tags = parser.find_proper_tags()
    print(proper_tags)
    # Calculate the number of marks to minus.
    total_marks_to_minus = 0
    exists = None
    corresponding_item = None
    for check in html_tag_data['tag_marks']:
        exists = False
        corresponding_item = None
        for item in proper_tags:
            corresponding_item = check
            if check['tag'] == item:
                exists = True
        if(not exists):
            total_marks_to_minus += corresponding_item['marks']
    webbrowser.get(determine_os()).open(html_file_path, 0, True)
    return total_marks_to_minus

print("We need to minus:" ,determine_marks(), " mark(s).")
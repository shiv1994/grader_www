import os, json
from html.parser import HTMLParser

# check_list = [
#     {'marks':1, 'tag':'html'},
#     {'marks':1, 'tag':'p'},
#     {'marks':1, 'tag':'a'},
#     {'marks':1, 'tag':'h1'},
#     {'marks':1, 'tag':'h2'},
#     {'marks':1, 'tag':'h3'},
#     {'marks':1, 'tag':'ul'},
#     {'marks':1, 'tag':'li'},
#     {'marks':1, 'tag':'ol'},
#     {'marks':1, 'tag':'div'},
#     {'marks':1, 'tag':'title'},
#     {'marks':1, 'tag':'body'},
#     {'marks':1, 'tag':'head'},
#     {'marks':1, 'tag':'h4'},
# ]

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

def determine_marks():
    # Get current working directory.
    cwd  = os.getcwd()
    # Load html file that will be checked.
    html_file = open(cwd + "/scripts/home.html", "r").read()
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
    return total_marks_to_minus

print("We need to minus:" ,determine_marks(), " mark(s).")
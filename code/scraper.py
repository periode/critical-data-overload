from bs4 import BeautifulSoup # this is our parser
import requests # this is our requester

TARGET_URL = "https://newyork.craigslist.org/search/mis"

# we define the function for our parser
def parseBody(body):
    soup = BeautifulSoup(body, 'html.parser')    
    results = []
        
    titleElements = soup.find_all('.cl-static-search-result')
    # we go through all the 
    for index, element in titleElements:
        title = element["title"] # gets the "title" attribute
        link = element.a["href"] # gets the "href" attribute of the <a> tag
        
        print("#{index}, {title} -> {link}")
        
        results.append("{index},{title},{link}")
    
    # and we write our results to a file
    TARGET_FILE = "./results_py.txt"
    with open(TARGET_FILE, 'a') as the_file:
        the_file.write(",".join(results))
    print("wrote to {TARGET_FILE}")

r = requests.get(TARGET_URL)


if r.status_code == 200:
    parseBody(r.text)



# these two packages need to be installed via `pip install beautifulsoup4 requests`
from bs4 import BeautifulSoup # this is our parser
import requests # this is our requester

TARGET_URL = "https://newyork.craigslist.org/search/mis"

# we define the function for our parser
def parseBody(body):
    soup = BeautifulSoup(body, 'html.parser')    
    results = []
        
    # we find all <li> elements with class "cl-static-search-result"
    titleElements = soup.find_all("li", "cl-static-search-result")
    
    # we go through all the elements
    for (index, element) in enumerate(titleElements):
        title = element["title"] # gets the "title" attribute
        link = element.a["href"] # gets the "href" attribute of the <a> tag
        
        print(f"#{index}, {title} -> {link}")
        
        results.append(f"{index},{title},{link}")
    
    # and we write our results to a file
    TARGET_FILE = "./results_py.txt"
    with open(TARGET_FILE, 'a') as the_file:
        the_file.write("\n".join(results))
    print(f"wrote to {TARGET_FILE}")

r = requests.get(TARGET_URL)


if r.status_code == 200:
    parseBody(r.text)



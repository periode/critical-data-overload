import requests
from bs4 import BeautifulSoup

# first step is downloading the webpage (we 
# use "requests")

# second step is _parsing_ (going through the text) (we use "beautifulsoup")

def scrapePage(target_url):
    # here, we download the webpage and save it in the myRequest variable
    myRequest = requests.get(target_url)

    # we save the result into a variable called webpageText
    webpageText = myRequest.text

    soup = BeautifulSoup(webpageText, 'html.parser')

    all_posts = soup.find_all('li', 'cl-static-search-result')

    # here we create an empty list to store all of our results
    results = []
    for post in all_posts:
        title = post['title']
        
        # i want the <a> element inside the post
        linkElement = post.a
        # i want the attribute "href" of the linkElement
        link = linkElement['href']
        
        # once we found the title and the link for one post
        # we add it to our results
        results.append(f"{title},{link}")
        
    return results
        
        
all_data = []
all_cities = ["newyork", "chicago", "detroit", "losangeles", "austin"]

for city in all_cities:
    data = scrapePage(f"https://{city}.craigslist.org/search/mis")
    all_data += data

# third step is saving the data to a file
with open("results.txt", 'w') as f:
    f.write("\n".join(all_data))

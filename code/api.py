# in this program, we will try to find out all of the stock images used on popular tech news
import requests

def getPage(target):
    r = requests.get(target)
    data = r.json() # here we get the data as json
    stock_images = [] # we ready our empty list to fill with our results
    for d in data:
        image_url = d['jetpack_featured_media_url'] # we know this is the field with the image thanks to our inspection
        if "Getty" in image_url: #we check if the image is a stock image
            # print(image_url)
            stock_images.append(image_url)
            
    # print(f"found {len(stock_images)} results")
    return stock_images

pages = ["1", "2", "3"]
all_results = []
for page in pages:
    res = getPage(f"https://techcrunch.com/wp-json/wp/v2/posts?per_page=100&page={page}&context=embed")
    all_results += res

print(f"found {len(all_results)} results.")

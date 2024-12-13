# in this program, we will try to find out all of the stock images used on popular tech news
import requests # this is the package to make a request for a web page

def getPage(target):
    # first, we request the page
    r = requests.get(target)
    
    # here we get the data as json
    all_posts = r.json()
    
    stock_images = [] # we ready our empty list to fill with our results
    for single_post in all_posts:
        image_url = single_post['jetpack_featured_media_url'] # we know this is the field with the image thanks to our inspection
        if "Getty" in image_url or "getty" in image_url: # we check if the image is a stock image (if the image file contains the word "Getty")
            # print(image_url)
            stock_images.append(image_url)
            
    # print(f"found {len(stock_images)} results")
    return stock_images



all_results = []
for page in range(1, 20):
    print(f"scraping page #{page}")
    result = getPage(f"https://techcrunch.com/wp-json/wp/v2/posts?per_page=100&page={page}&context=embed")
    all_results += result



print(f"found {len(all_results)} results.")

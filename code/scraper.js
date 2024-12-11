// first we need to import the `cheerio` module, which will allow us to go through the webpage
// to install cheerio, use `npm install cheerio` in the same folder as your code
const cheerio = require("cheerio");
const fs = require("fs")
const TARGET_URL = "https://newyork.craigslist.org/search/mis"

// this is our function to get the webpage
const getPage = async (url) => {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const body = await response.text();
        return body
    } catch (error) {
        console.error("error:",error);
        return ""
    }
}

// this is our function to parse the results of our request and look for specific elements
const parseBody = (body) => {
    // if there is no body, we don't do anything (i.e. return immediately)
    if(body == ""){
        return
    }
    // we load the body in cheerio
    const $ = cheerio.load(body)
    
    // we prepare an empty array to get our results
    let results = []

    // we get every element with the `cl-static-search-result` class
    // since (it's the one that contains both the <a> and the <div class="title">)
    const titleElements = $('.cl-static-search-result')
    titleElements.each((index, element) => {
        const title = $(element).find(".title").text()
        const link = $(element).find("a").attr().href
        
        console.log(index, title, "->", link);

        // we add it to our results array
        results.push(`${index},${title},${link}`)
    })

    // now, we save our results to a file
    const TARGET_FILE = "./results_js.txt"
    fs.writeFileSync(TARGET_FILE, results.join("\n"))
    console.log("wrote to",TARGET_FILE)
}

// here we chain it all together: first get the page, then parse the body, and watch out for any errors
getPage(TARGET_URL)
    .then(parseBody)
    .catch((e) => console.error(e))


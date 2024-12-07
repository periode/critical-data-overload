# Critical Data Overload: Introduction

---

## Plan for the day

---

This morning:

- introduction (me, you, this class)
- thinking about data, practically and critically
- examples of work

---

This afternoon:

- data collection techniques: scraping and requesting
- scraping in HTML: the craigslist example
- using artoo.js

---

## Introduction

---

Pierre Depaz ([pierredepaz.net](https://pierredepaz.net))

political science, game design, comparative literature

i'm curious about how code affects our thought processes.

---

You ? Name, experience with programming, why did you come to this class?

---

### WHAT

This class is about critically thinking about data through direct engagement.

---

### WHY

- what is data? when does it become information? what is this information about?
- how is data distributed? how is it taken apart and recombined? what do technical systems reveal about data providers?
- how do we re-present data in order to change its interpretation?

---

### HOW

Over the next 5 days, we will collaboratively build new corpora of online data.

1. Identifying ways to think about data as a kind of corpus (research, conceptual thinking)
2. Learning the technical tools to acquire this data, and render it usable (programming, JS, Python)
3. Reflecting on how to interface this data (sketching)

---

## Thinking about data

---

What is data?

---

The mathematical theory of communication is the disappearance of meaning

---

What is metadata?

---

Data vs. capta

---

Data as the by-product of systems

---

Data is the new oil?

---

From data to information, the role of interpretation

---

What agency do we have when faced with a deluge of data?

---

## Examples

---

- Sam Lavigne's [Baabaa](https://lav.io/projects/baabaa/), [C-Span 5](https://lav.io/projects/cspan-5/), [Occupied B&B](https://lav.io/projects/occupied-bnb/) (and the [accompanying piece](https://www.thenation.com/article/archive/airbnb-settlement-lawsuit-palestinian-challenge/))
- Winnie Soon's [Unerasable Characters](https://siusoon.net/projects/unerasablecharacters-i)
- Miao Ying's [Blind Spot](https://anthology.rhizome.org/blind-spot)
- Pierre Depaz's [Real Time Sound Cloud](https://realtime.enframed.net)
- Anonymous' [F*ck everyword](https://x.com/fuckeveryword)
- Jason Salavon's [100 Special Moments](http://salavon.com/work/SpecialMoments/)
- Lev Manovich and his team's [Selfie City](https://selfiecity.net)
- Mimi Onuha's [Missing Datasets](https://github.com/MimiOnuoha/missing-datasets)
- Disnovation.org's [Pirate Cinema](https://disnovation.org/piratecinema.php)
- Kyle McDonald's [Spotify Serendipity](https://youtu.be/mD7vs_Vw_P0?si=HmtWzD_R_zEqV_x6)
- Luke DuBois's [A More Perfect Union](https://www.lukedubois.com/projects-2/perfect) and [Billboard](https://www.lukedubois.com/projects-2/billboard)
- Mark Hansen and Ben Rubin's [Moveable Type](https://vimeo.com/113240712)
- Aaron Swartz and Taryn Simon's [Image Atlas](https://anthology.rhizome.org/image-atlas)
- Nicolas Malevé's [12 Hours of ImageNet](https://www.youtube.com/watch?v=PC60JL-lMzA)
- Josh Begley's [Prison Map](http://prisonmap.com/about) and [Drone Stream](https://x.com/dronestream) and [Condolences](https://theintercept.co/condolences/)

---

MAHLZEIT

---

## Working with data

---

Installing our tools

- Web Browser (please no Safari)
- NodeJS
- Python

---

Data __types__

---

Data __structures__

---

Data __markups__

---

Manipiulating in a __programming language__

---

## Gathering data

---

__Scraping__ is the process of taking apart a webpage.

If you see it on your browser, it's already in your computer.

---

Practical example in the browser

---

Developer tools are your best friends!

---

Automating it!

---

APIs

---

## Craigslist example

---

1. Analysis
2. Testing
3. Navigating

---

Analysis

- what does the site architecture look like?
- how do i get from one page to another?
- what does the markup looklike?
- are there any `class` or `id` we can use?
- is there any pattern we can build on?

---

Testing

- write a small __page scraper__ that goes directly to a specific page
- log the elements as we find them
- save them to a file

---

Navigating

- write small piece of code that visits every page
- connect it to our __page scraper__

---

## Homework

- __read__: [_Scrapism, A Manifesto_](https://read.dukeupress.edu/critical-ai/article-abstract/doi/10.1215/2834703X-10734046/382464/Scrapism-A-Manifesto) by Sam Lavigne
- __think__: what kinds of data would you like to collect? which system are you interested in?

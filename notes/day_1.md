# Critical Data Overload: Introduction

---

## Plan for the day

---

This morning:

- introduction (me, you, this workshop)
- thinking about data, practically and critically
- examples of work

---

This afternoon:

- data collection techniques: scraping and requesting
- scraping in HTML: the craigslist example

---

## Introduction

---

Pierre Depaz ([pierredepaz.net](https://pierredepaz.net))

political science, game design, comparative literature

i'm curious about how code affects our ways of thinking and acting.

---

You ? Name, experience with programming, why did you come to this workshop?

---

### What

---

This workshop focuses on critically thinking about data through direct engagement.

Collecting datasets to better understand what it is, where it comes from, and what it can mean.

<!-- this means understanding and working with data in a very practical way: through the systems we often interface with -->

---

### Why

---

To provide concrete answers to some questions:

- what is data? when does it become information? what is this information about?
- how is data distributed? how is it taken apart and recombined? what do technical systems reveal about data providers?
- how do we re-present data in order to change its interpretation?

(also as a starting point for Helin's class next semester)

---

### How

Until Monday, we will collaboratively build new corpora of online data.

1. __Identifying__ ways to think about data as a kind of corpus (research, conceptual thinking)
2. __Using__ the technical tools to acquire this data, and render it usable (programming, JS, Python)
3. __Reflecting__ on how to interface this data (sketching)

<!-- aka we create our own datasets in groups -->

---

## Thinking about data

---

What is data?

<!-- data is a pattern of symbols which can be made meaningful -->

---

Data is a pattern of symbols which can be made meaningful.

---

What is metadata?

<!-- data about data, sketching things in the negative -->

---

Data is the new oil?

<!-- Airbnb and Facebook started by scraping -->

---

Data as the by-product of systems: data vs. capta.

<!-- Data comes from "given" in latin, but it's not alway given, rather it's "taken", captured, capta -->

---

What is the difference between data and information?

---

The mathematical theory of communication and __the disappearance of meaning__.

<!-- so we need to represent, in order to interpret -->

---

What agency do we have when faced with a deluge of data? How do we make sense of it?

<!-- Distance, or pivot is one way of doing it. Art is one way of providing a different perspective -->

---

Data is the __raw material__ of digital technologies. It only becomes information through __representation__, which facilitates __interpretation__.

---

## Examples

---

Politics:

- Sam Lavigne's [Get Well Soon](https://lav.io/projects/get-well-soon/), [C-Span 5](https://lav.io/projects/cspan-5/), [Occupied B&B](https://lav.io/projects/occupied-bnb/) (and the [accompanying piece](https://www.thenation.com/article/archive/airbnb-settlement-lawsuit-palestinian-challenge/))
- Winnie Soon's [Unerasable Characters](https://siusoon.net/projects/unerasablecharacters-i)
- Miao Ying's [Blind Spot](https://anthology.rhizome.org/blind-spot)
- Jack Sweeney's [ElonJet](https://mastodon.social/@elonjet)
- Lawrence Abu Hamdan's [Air Pressure](https://airpressure.info)
- Emma Sheffer's [Insta Repeat](https://www.instagram.com/insta_repeat)
- Luke DuBois's [A More Perfect Union](https://www.lukedubois.com/projects-2/perfect) and [Billboard](https://www.lukedubois.com/projects-2/billboard)
- Mark Hansen and Ben Rubin's [Moveable Type](https://vimeo.com/113240712)
- Josh Begley's [Prison Map](http://prisonmap.com/about) and [Drone Stream](https://x.com/dronestream) and [Condolences](https://theintercept.co/condolences/)

Visual Culture:

- Lev Manovich and his team's [Selfie City](https://selfiecity.net)
- Jason Salavon's [100 Special Moments](http://salavon.com/work/SpecialMoments/)
- Nicolas Malevé's [12 Hours of ImageNet](https://www.youtube.com/watch?v=PC60JL-lMzA)
- Aaron Swartz and Taryn Simon's [Image Atlas](https://anthology.rhizome.org/image-atlas)

Multimedia:

- [Truth and Quantity](https://truth-and-quantity.com)
- Riley Walz's [IMG_0001](https://walzr.com/IMG_0001)
- Pierre Depaz's [Real Time Sound Cloud](https://realtime.enframed.net)
- Hatnote's [Listen to Wikipedia](http://listen.hatnote.com)
- Kyle McDonald's [Spotify Serendipity](https://youtu.be/mD7vs_Vw_P0?si=HmtWzD_R_zEqV_x6)
- Disnovation.org's [Pirate Cinema](https://disnovation.org/piratecinema.php)

Misc:

- Mimi Onuha's [Missing Datasets](https://github.com/MimiOnuoha/missing-datasets)
- [Flickr's Data Lifeboat](https://www.flickr.org/programs/content-mobility/data-lifeboat/)

---

Critical data explorations is shaping a material to represent something about a system (critically, poetically, both)

---

MAHLZEIT

---

## Gathering data

---

__Scraping__ is the process of taking apart a webpage.

If you see it on your browser, it's already in your computer.

---

__Interfacing__ is the process of asking for data from a specialized service (an _Application Programming Interface_)

---

Both can be automated!

---

## Working with web data

---

Data __markups__

```html
<element attribute="value">some text</element>
```

---

Anatomy of a webpage a.k.a Developer Tools are your best friends!

(please don't use safari)

- menu > more tools > developer tools > elements

---

## Craigslist example

---

First things first, installing tools:

- Python
- NodeJS

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

__Exercise_

find a news website and extract all the headlines you can find with one or more particular words (e.g. "says", "trial").

---

## Homework

- __read__: [_Scrapism, A Manifesto_](https://read.dukeupress.edu/critical-ai/article-abstract/doi/10.1215/2834703X-10734046/382464/Scrapism-A-Manifesto) by Sam Lavigne
- __think__: what kinds of data would you like to collect? which system are you interested in?

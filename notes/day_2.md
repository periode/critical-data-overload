# Critical Data Overloads: Acquisition

---

## Plan for the day

---

This morning:

- discussing scrapism
- identifying a corpus

---

This afternoon:

- interfacing with an API
- discussing corpus ideas and tactics

---

## Scrapism: A Manifesto

---

What did you think of the reading?

---

The open and the invisible

<!-- 

Where does the data come from, how do systems communicate with one another?

The machine exchange of data, back to Shannon

-->

---

The web is a database

<!--

maybe discussing a bit more how the web works, what is a URL, what is a server

-->

---

Understanding systems by looking in their databases

<!--

Frag den Staat

FOIA

How you classify things reveal things about you (miller, artefacts). Taste in spotify is kinda machine-generated

-->

---

From machine __in to__ the machine

<!-- 

Machine in the Kafka sense of the term.

The mechanical processing of standardized inputs.

What kinds of machines can we think of?

School, hospital, military, entertainment

-->

---

From machine __out of__ the machine.

<!--

By re-contextualizing, you give a different interpretation, a different light on the same data.

-->

---

## Identifying a corpus

---

Turning a dataset into a corpus.

The purpose of a corpus is to learn something from it, and to communicate these findings to others.

<!--

A corpus is something that can be studied, that has an interest in terms of research. It means we can learn things from it.

But what things?

First, what are the kinds of things to consider when imagining a corpus?

-->

---

__Intra__-textuality is the comparison of different parts of the same text, and allows to reveal repeating patterns.

---

It can highlight some broad themes, blurry but evocative

"I am 20 years old and..."

[r/googlepoems](https://www.reddit.com/r/googlepoems/)

---

It can highlight some structures.

![Paolo Cirio's Art Commodities, 2014](./assets/cirio_art_system.jpg)

---

__Inter__-textuality is the comparison of parts of different texts, showing how they are connected.

![Alfred Barr, Cubism and Abstract Art, 1936](./assets/barr_cubism_abstract_art.jpg)

![Hank Willis Thomas, Colonialism and Abstract Art, 2020](./assets/thomas_colonialism_abstract_art.jpg)

---

A comparative approach puts the focus on __what is different__ and __what is the same__.

---

Finding a topic:

- What __culture__ do you want to explore?
- What __system__ do you want to reveal?
- What __themes__ do you want to address?

<!--

Culture is about the imaginaries, the practices, the common beliefs that link us together. How people express themselves, e.g.

System is about the invisible connections and arrangements that are fixed in place in order to achieve something.

10 minutes to write down 4-5 of them

-->

---

Presenting our ideas (Miro board)

---

Finding the data:

- How does this data manifest itself on the web?
- What are the organizations who __produce__ this data? What are the organizations that  What are the organizations who __use__ this data?
- Is it on a webpage? on an app? served over an API? Do you have to cross-reference multiple sources to find it?

---

Creative constraints:

- It should not already exist.
- It should be large (> 500) (a change in quantity can become a change in quality).

<!-- Take the rest of the morning to start googling around -->

---

MAHLZEIT (think about it over lunch)

---

## Working with an API

---

The overal model:

You < API > Data

![A simple API model](./assets/api.png)

---

Moving parts:

- the data models
- the access key

---

The data model is how the data is represented by a specific organization.

For instance, YouTube, SoundCloud and Spotify do not represent a song the same way.

---

The access key is a unique identifier that protects the organization from abuse.

You can either __apply for one__ or __borrow one__.

---

Example: getting all tracks on soundcloud that have less than 5 plays.

1. examining the soundcloud model
2. borrowing a key
3. requesting a track
4. starting somewhere

---

## Strategies and tactics

---

Group work to figure out how exactly you're going to get this data:

- what are the sources? how accessible are they? are there __proxies__? is there anything missing from them?
- what are the data models? what are the markups?
- what are the most appropriate tools to tackle the issue? are there any obvious problems that need to be solved?

Test early, fail early, solve early!

---

## Homework

- __consider__ consulting Pierre over the weekend for conceptual and technical issues (room 320).
- __collect__ your corpus, and come ready to present it to your classmates.

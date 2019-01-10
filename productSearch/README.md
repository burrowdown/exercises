### API exercise for WalmartLabs

To run:

`npm install`
`npm start`
hit `localhost:3000/items/<search keyword>`


#### Apologies

First of all, I sincerely apologize that I don't have the time to give this exercise the attention it deserves. I'm somehow even busier than I was when I was employed full time. I appreciate the design of this problem, there are lots of interesting questions that I wish I could take the time to explore. I found an hour or two last week to play around with hapi for the first time. This week I had about an hour to spend implementing a solution, and I came up with a basic outline in that time.

In lieu of actually being able to design a robust solution, I'll do my best to describe what I *would* do, if I had more than an hour to devote to it.


#### Next steps

* Most importantly and most obviously, **unit tests**. It's embarrassing to even submit a code sample without tests, but I got a little ambitious and tried to use lab, hoping to stay in the hapi world, before realizing that using a brand new-to-me testing framework wasn't going to happen in the limited time I have. If I could to it again I'd just use mocha.

* **Make serial API calls:**: You gave me 18 product IDs and the Product Lookup API accepts 20. Here's how I would approach a larger data set:
  * chunk the id's coming in from the CSV into groups of 20 (or fewer)
  * (this would be a good place to do some data validation on the id's)
  * for each chunk, make an API call
  * make those calls serially

 * **Search both the short and long descriptions:** Not all products have a long description, and there may be other fields worth searching while we're at it. This should be quick to implement, I'd do it right now if I wasn't going to be late for an appointment!


#### Above and beyond

These are a few things that I wouldn't implement for a coding exercise, but would take into consideration for production code:

 * **Refresh data:** Right now the product data is fetched when the server is started, and is never refreshed. How often are we expecting product data to be updated? How expensive are API calls? We could get fresh data from the Product Search API nightly, or every 100 ms, or every time the keyword search endpoint is hit, etc., depending on the relative cost of available resources.

* **More robust searching:** String.includes is good enough for a coding exercise, but we can probably do better if this API is going to be used externally. I'd look into using Elasticsearch, or something like that.

* **Local storage considerations:** I'm storing the whole product data object in memory, because for 18 products why not? For a larger data set, I'd consider just pulling out the product information that's actually relevant, (in this design, just the descriptions and id,) and storing only that.

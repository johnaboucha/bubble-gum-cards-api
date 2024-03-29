# Documentation

<h2 id="overview">Overview</h2>

The Bubble Gum Cards API provides access to a curated set of baseball cards. The collection is unique in that the individual cards have been categorized by the contents of their photograph. Individually, the cards have little value by themselves but when grouped together, they become priceless. New cards are added periodically.

A basic app using this API can be found at [https://bubblegumcards-1-m1415162.deta.app](https://bubblegumcards-1-m1415162.deta.app).

The inspiration for this project is found in the blog post [How To Collect Baseball Cards](https://johnboucha.com/writing/how-to-collect-baseball-cards/).

<h2 id="getting-started">Getting started</h2>

Let's make your first request to the Bubble Gum Cards API.

Open up Terminal, Postman, or another tool to make a request for a resource. In the example below, a request is made to the baseball card with an ID equal to 1.

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/cards/1
</code></pre>


Here is the response.

<pre><code class="hljs language-html">HTTP/1.0 200 OK
Content-Type: application/json
{
	"id": 1,
	"year": 1989,
	"manufacturer": "Fleer",
	"player": "Billy Ripken",
	"series": "",
	"number": "616",
	"description": "Player is holding a bat with the words Fuck Face written on the end of the handle.",
	"category": "Priceless",
	"parallel": "",
	"image": "1989-fleer-ripken.jpg"
}
</code></pre>

<h3 id="base">Base URL</h3>

The Base URL is the root URL that all requests will begin. The documentation assumes you are appending all endpoints to the Base URL to make requests.

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/
</code></pre>

<h3 id="authentication">Authentication</h3>

The Bubble Gum Cards API is free and open. No authentication is required to query data using GET requests. Other HTTP method requests are not available.

<h3 id="query-options">Query String Options</h3>

The API includes ```skip``` and ```top``` options when querying a resource. Skip excludes the first _N_ items of a resource and top limits the response to _N_ items. The default value of ```skip``` is 0. The default value of ```top``` is 9.

As an example, the following request will return 5 cards starting from the 10th card.

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/cards/?skip=9&top=5
</code></pre>

<h3 id="search">Search</h3>

All resources support a search parameter that filters the results returned. Searches are not case sensitive and partial matches on field contents are returned.

An example of a search query is shown below.

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/cards/?search=steve</code></pre>

<h2 id="resources">Resources</h2>

<h3 id="root">Root</h3>

The Root resource path returns available resources within the API.

Example request:

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/
</code></pre>

Example response:

<pre><code class="hljs language-html">HTTP/1.0 200 OK
Content-Type: application/json
{
	"cards": "/api/cards/",
	"manufacturers": "/api/manufacturers/",
	"players": "/api/players/",
	"teams": "/api/teams/",
	"categories": "/api/categories/"
}
</code></pre>

Resources:

- ```cards``` The root URL for Cards resources
- ```manufacturers``` The root URL for Manufacturers resources
- ```players``` The root URL for Players resources
- ```teams``` The root URL for Teams resources
- ```categories``` The root URL for Categories resources

<h3 id="cards">Cards</h3>

A Card resource is an individual card within the collection.

Endpoints

- ```/cards/``` gets all the card resources
- ```/cards/:id/``` gets specific card by its ID

Example request:

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/cards/2</code></pre>

Example response:

<pre><code class="hljs language-html">HTTP/1.0 200 OK
Content-Type: application/json
{
	"id": 2,
	"year": 1989,
	"manufacturer": "ProCards",
	"player": "Kieth Comstock",
	"series": "Minor League Team Sets",
	"number": "14",
	"description": "A baseball is impacting the player's crotch",
	"category": "Priceless",
	"parallel": "",
	"image": "1989-procards-comstock.jpg"
}
</code></pre>

Attributes:

- ```year``` the year the card was produced
- ```manufacturer``` the company who manufactured the card
- ```player``` the baseball player or athlete
- ```series``` specified if card is a member of a non-regular set
- ```number``` the card number
- ```description``` a description of the card's photograph
- ```category``` the category the card belongs to in the collection
- ```parallel``` specified if card is a parallel version
- ```image``` name of the reference image on the server

Searchable fields:

- ```player```
- ```description```

Query parameters:

- ```category```

An example query using the category parameter is shown below:

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/cards/?category=telephone</code></pre>

Example response:

<pre><code class="hljs language-html">HTTP/1.0 200 OK
Content-Type: application/json
[{
	"id": 28,
	"year": 1994,
	"manufacturer": "Upper Deck",
	"player": "Cal Ripken Jr",
	"series": "Collector's Choice",
	"number": "240",
	"description": "",
	"category": "Telephone",
	"parallel": "",
	"image": ""
},
{
	"id": 29,
	"year": 1996,
	"manufacturer": "Stadium Club",
	"player": "Todd Zeile",
	"series": "",
	"number": "420",
	"description": "",
	"category": "Telephone",
	"parallel": "",
	"image": ""
},
...]
</code></pre>

<h3 id="manufacturers">Manufacturers</h3>

A Manufacturer resource is a single card manufacturer found within the collection.

Endpoints

- ```/manufacturers/``` gets all the manufacturer resources
- ```/manufacturers/:id/``` gets specific manufacturer by its ID

Example request:

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/manufacturers/1</code></pre>

Example response:

<pre><code class="hljs language-html">HTTP/1.0 200 OK
Content-Type: application/json
{
	"id": 1,
	"name": "Topps",
	"year_founded": "1938",
	"year_defuct": "",
	"fate": "",
	"headquarters": "New York, NY",
	"website": "https://www.topps.com/",
	"revenue": "$560 million",
	"employees": "422",
	"address": "1 Whitehall Street New York, NY 10004"
}</code></pre>

Attributes:

- ```name``` the name of the manufacturer
- ```year_founded``` the year the manufacturer was established
- ```year_defunct``` the year the manufacturer went bankrupt or was sold
- ```fate``` description of what happened after manufacturer went defunct
- ```headquarters``` the location of the manufacturer's main office
- ```website``` the manufacturer's website
- ```revenue``` the manufacturer's actual or estimated revenue
- ```employees``` the number of manufacturer's employees
- ```address``` the street address of the manufacturer

Searchable fields

- ```name```

<h3 id="players">Players</h3>

A Player resource is a single player found within the collection.

Endpoints

- ```/players/``` gets all the player resources
- ```/players/:id/``` gets specific player by their ID

Example request:

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/player/3</code></pre>

Example response:

<pre><code class="hljs language-html">HTTP/1.0 200 OK
Content-Type: application/json
{
	"id": 3,
	"first_name": "Barry",
	"last_name": "Bonds",
	"position": "Left Field",
	"birth_date": "1964-07-24",
	"death_date": "",
	"throws": "left",
	"bats": "left",
	"height": "6' 1\"",
	"weight": "185"
}</code></pre>

Attributes:

- ```first_name``` the player's first name
- ```last_name``` the player's last name
- ```position``` the player's position
- ```birth_date``` the player's birth date
- ```death_date``` the date of the player's death
- ```throws``` the hand the player throws with
- ```bats``` the side the player bats from
- ```height``` the player's height
- ```weight``` the player's weight

Searchable fields:

- ```first_name```
- ```last_name```

<h3 id="teams">Teams</h3>

A Team resource is a single team found within the collection.

Endpoints

- ```/teams/``` gets all the team resources
- ```/teams/:id/``` gets specific team by its ID

Example request:

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/team/3</code></pre>

Example response:

<pre><code class="hljs language-html">HTTP/1.0 200 OK
Content-Type: application/json
{
	"id": 3,
	"location": "Montreal",
	"name": "Expos",
	"league": "National League",
	"league_level": "major",
	"year_established": "1969",
	"year_defunct": "2004"
}</code></pre>

Attributes:

- ```location``` the team's location
- ```name``` the team's name
- ```league``` the league that the team is a member of
- ```league_level``` the league level the team participates in
- ```year_established``` the year the team was formed
- ```year_defunct``` the year the team was sold or disbanded

Searchable fields:

- ```location```
- ```name```

<h3 id="categories">Categories</h3>

The Category resource returns all the categories found within the collection.

Endpoints

- ```/categories/``` gets all the categories resources

Example request:

<pre><code class="hljs language-html">https://bgcardsapi-1-u6196911.deta.app/api/categories/</code></pre>

Example response:

<pre><code class="hljs language-html">HTTP/1.0 200 OK
Content-Type: application/json
{
	"categories": [
		"Alliteration",
		"Bubble Gum",
		"Camera",
		"Celebrity",
		"Crotch Bat",
		"Fly Ball",
		"Flying Helmet",
		"Priceless",
		"Tagged Out",
		"Telephone"
	]
}</code></pre>

<h2 id="code-examples">Example Code</h2>

<h3>Python</h3>

Use the ```requests``` library in Python to make GET requests.

	from requests import get

	response = get('https://bgcardsapi-1-u6196911.deta.app/api/cards/')

	cards = list(response.json())

	for card in cards:
		print(card['year'], card['manufacturer'], card['player'])


### Go

Use the ```net/http``` package in Go's standard library to make GET requests.

	package main

	import (
		"encoding/json"
		"fmt"
		"io/ioutil"
		"log"
		"net/http"
	)

	type Card struct {
		CardID       int
		Year         int
		Manufacturer string
		Player       string
		Series       string
		Card_number  string
		Description  string
		Category     string
		Parallel     string
		Image        string
	}

	func main() {
		response, err := http.Get("https://bgcardsapi-1-u6196911.deta.app/api/cards/")
		if err != nil {
			log.Fatalln(err)
		}

		body, err := ioutil.ReadAll(response.Body)
		if err != nil {
			log.Fatalln(err)
		}

		var cards []Card
		json.Unmarshal(body, &cards)

		for _, card := range cards {
			fmt.Println(card.Year, card.Manufacturer, card.Player)
		}
	}

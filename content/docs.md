# Documentation

## Overview

The Bubble Gum Cards is a JSON-based API that provides access to a curated set of trading cards, mostly baseball, that have been categorized by the contents of their photograph.

All requests are made to endpoints appended to the root URL: ```/api/```

An example frontend using the API can be found at: ```https://example.com```

## Getting started

Making a request to the Bubble Gum Cards API is easy.

Open up a Terminal, Postman, or another tool to make a request for a resource. In the example below, a request is made to the baseball card with the ID 1.


	http://localhost:8000/api/cards/1


Here is the response.

	{
	"id": 1,
	"year": 1989,
	"manufacturer": "Fleer",
	"player": "Billy Ripken",
	"series": "",
	"number": "616",
	"description": "Player is holding a bat with the words Fuck Face written on the end of the handle.",
	"category": "Nutty",
	"parallel": "",
	"image": "1989-fleer-ripken.jpg"
	}

### Base URL

The Base URL is the root URL that all requests start with. The documentation assumes you are appending all endpoints to the Base URL to make requests.

	https://example.com

### Authentication

Bubble Gum Cards API is a free and open API. No authentication is required to query data using GET requests. No other HTTP methods are available.

### Search

All resources support a search parameter that filters the results returned. Searches are not case sensitive and partial matches on field contents are returned. An example of a search query is shown below.

	https://example.com/api/cards/?search=steve

## Resources

### Root

The Root resource path returns available resources within the API.

Example request:

	https:/example.com/api/

Example response:

	HTTP/1.0 200 OK
	Content-Type: application/json
	{
		"cards": "/api/cards/",
		"manufacturers": "/api/manufacturers/",
		"players": "/api/players/",
		"teams": "/api/teams/"
	}

Attributes:

- ```cards``` The root URL for Cards resources
- ```manufacturers``` The root URL for Manufacturers resources
- ```players``` The root URL for Players resources
- ```teams``` The root URL for Teams resources

### Cards

A Card resource is an individual card within the collection.
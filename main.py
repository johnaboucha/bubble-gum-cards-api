from fastapi import FastAPI, Request
from routers import cards, manufacturers, players, teams, categories
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
import markdown

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
	with open('content/docs.md', 'r') as f:
		text = f.read()
		html = markdown.markdown(text)

	return templates.TemplateResponse("docs.html", {"request": request, "content":html})


@app.get("/api")
def root():
	return {
		"cards": "/api/cards/",
		"manufacturers": "/api/manufacturers/",
		"players": "/api/players/",
		"teams": "/api/teams/"
	}

app.include_router(cards.router)
app.include_router(players.router)
app.include_router(manufacturers.router)
app.include_router(teams.router)
app.include_router(categories.router)
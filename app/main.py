from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader, select_autoescape

from app.data.profile import PROFILE

APP_DIR = Path(__file__).resolve().parent
ROOT_DIR = APP_DIR.parent
STATIC_DIR = ROOT_DIR / "static"
TEMPLATES_DIR = APP_DIR / "templates"

jinja_env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape(["html"]),
)

app = FastAPI(title="Portfolio", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    template = jinja_env.get_template("index.html")
    html = template.render(request=request, profile=PROFILE)
    return HTMLResponse(content=html)

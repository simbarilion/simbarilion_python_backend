from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader, select_autoescape
from starlette.responses import Response
from starlette.types import Scope

from app.data.profile import PROFILE

APP_DIR = Path(__file__).resolve().parent
ROOT_DIR = APP_DIR.parent
STATIC_DIR = ROOT_DIR / "static"
TEMPLATES_DIR = APP_DIR / "templates"

# Browser cache for CSS/JS/images/overviews (7 days)
STATIC_CACHE_HEADERS = {"Cache-Control": "public, max-age=604800"}

jinja_env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape(["html"]),
)


class CachedStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope: Scope) -> Response:
        response = await super().get_response(path, scope)
        if response.status_code == 200:
            response.headers.update(STATIC_CACHE_HEADERS)
        return response


app = FastAPI(title="Portfolio", docs_url=None, redoc_url=None)
app.mount("/static", CachedStaticFiles(directory=STATIC_DIR), name="static")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(
        STATIC_DIR / "favicon.svg",
        media_type="image/svg+xml",
        headers=STATIC_CACHE_HEADERS,
    )


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    template = jinja_env.get_template("index.html")
    html = template.render(request=request, profile=PROFILE)
    # HTML without long cache — content changes often via profile.py
    return HTMLResponse(
        content=html,
        headers={"Cache-Control": "no-cache"},
    )

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import __version__
from app.api.v1.routers import v1


app = FastAPI(
    title="Dotflow",
    description="Dotflow Server API",
    version=__version__
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(v1, prefix="/v1")

templates = Jinja2Templates(directory="app/templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )


@app.get("/status", include_in_schema=False)
def get_status():
    """Get status of messaging server."""
    return ({"status": "it's alive"})

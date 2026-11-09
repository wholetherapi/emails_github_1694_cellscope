from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import anndata as ad
from app.plotting import umap_figure

app = FastAPI(title="CellScope")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/umap")
def umap(dataset: str):
    adata = ad.read_h5ad(dataset)
    return umap_figure(adata)

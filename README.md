# CellScope

CellScope is an internal, interactive dashboard for exploring single-cell atlases.
It started as a weekend tool for the Rao lab and has grown into a general-purpose
viewer used across projects.

> This repository is **not** the code release for any publication. It does not
> implement a paper method; use it only for exploratory data visualisation.

## Layout

- `app/main.py` — FastAPI application entry point
- `app/plotting.py` — UMAP and marker-gene plotting helpers
- `templates/index.html` — minimal dashboard shell
- `requirements.txt` — runtime dependencies

## Running

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

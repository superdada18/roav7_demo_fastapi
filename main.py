from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Utilisation de Jinja2 pour les templates HTML
templates = Jinja2Templates(directory="templates")

# Configuration des fichiers statiques (CSS, JS si nécessaire)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Base de données fictive (en mémoire)
product_data = [{
    "id": 1,
    "name": "Produit A",
    "price": 10.99,
    "stock": 10
    },
    {
    "id": 2,
    "name": "Produit B",
    "price": 20,
    "stock": 5
    },
    {
    "id": 3,
    "name": "Produit C",
    "price": 30,
    "stock": 2
    }
]

@app.get("/", response_class=HTMLResponse)
async def display_product(request: Request):
    """
    Affiche les détails du produit et un bouton pour réduire le stock.
    """
    return templates.TemplateResponse("index.html", {"request": request, "product": product_data})

@app.post("/update_stock/")
async def update_stock():
    """
    Réduit le stock de 1 si possible, puis redirige vers la page principale.
    """
    if product_data["stock"] > 0:
        product_data["stock"] -= 1
    # Redirige vers la page principale "/"
    return RedirectResponse(url="/", status_code=303)
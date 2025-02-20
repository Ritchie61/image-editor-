from fastapi import FastAPI
from app.routes import file_routes, text_routes, image_routes, font_routes

app = FastAPI(title="Image & Text Editor API")

# Include API routes
app.include_router(file_routes.router)
app.include_router(text_routes.router)
app.include_router(image_routes.router)
app.include_router(font_routes.router)

@app.get("/")
def home():
    return {"message": "Welcome to Image & Text Editor API"}

# Run using: uvicorn app.main:app --reload

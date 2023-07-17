from app.configurations.information import *

from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI

def create_server():
    # Create the FastAPI app. Setting server information
    app = FastAPI(
        title=title,
        description=description,
        version=version,
        contact=contact,
    )

    # Import Controllers/Routers

    # Startup and Shutdown Events
    @app.on_event("startup")
    async def startup():
        load_dotenv(find_dotenv())

    @app.on_event("shutdown")
    async def shutdown():
        pass
    
    return app

app = create_server()
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI

from .configurations.dbinit import database
from .configurations.information import *

from .controllers import factionController, unitController, skillTypeController, skillController, traitController, itemController

def create_server():
    # Create the FastAPI app. Setting server information
    app = FastAPI(
        title=title,
        description=description,
        version=version,
        contact=contact,
    )

    # Import Controllers/Routers
    app.include_router(factionController.router)
    app.include_router(unitController.router)
    app.include_router(skillTypeController.router)
    app.include_router(skillController.router)
    app.include_router(traitController.router)
    app.include_router(itemController.router)

    # Startup and Shutdown Events
    @app.on_event("startup")
    async def startup():
        app.state.db = database
        await app.state.db.connect()
        load_dotenv(find_dotenv())

    @app.on_event("shutdown")
    async def shutdown():
        await app.state.db.disconnect()
    
    return app

app = create_server()
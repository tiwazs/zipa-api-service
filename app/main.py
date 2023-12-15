from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .configurations.dbinit import database
from .configurations.information import *

from .controllers import FactionController, raceController, skillTypeController, skillController, traitController, itemController, effectController, unitSpecializationController, unitGenController, unitController, damageCalculationController

def create_server():
    # Create the FastAPI app. Setting server information
    app = FastAPI(
        title=title,
        description=description,
        version=version,
        contact=contact,
    )

    # Import Controllers/Routers
    app.include_router(damageCalculationController.router)
    app.include_router(FactionController.router)
    app.include_router(unitController.router)
    app.include_router(unitGenController.router)
    app.include_router(raceController.router)
    app.include_router(unitSpecializationController.router)
    app.include_router(skillTypeController.router)
    app.include_router(skillController.router)
    app.include_router(traitController.router)
    app.include_router(itemController.router)
    app.include_router(effectController.router)
    
    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    # Origins
    origins = [
        "*",
    ]

    # Cors
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

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
from .logs import logger

from fastapi import FastAPI, Response
from src.scenario import router as scenario_router
from src.dialogue import router as dialogue_router


app = FastAPI()

app.include_router(scenario_router.router)
app.include_router(dialogue_router.router)


@app.get('/')
def root():
    logger.info('Attempting to get root direction.')
    return Response('<h1>Interactive film API.</h1>')

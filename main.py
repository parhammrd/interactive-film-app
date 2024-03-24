import logging
from fastapi import FastAPI, Response


app = FastAPI()

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


@app.get('/')
def root():
    logger.info('Attempting to get root direction')
    return Response('<h1>Interactive film API.</h1>')

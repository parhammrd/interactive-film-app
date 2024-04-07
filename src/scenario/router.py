import json
from src.logs import logger

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from . import schemas


router = APIRouter(prefix='/scenario', tags=['scenario'])


@router.post('/save-chapters/')
async def save_chapters(chapterslist: schemas.ChapterList):
    try:
        validated_data = schemas.ChapterList.model_validate(chapterslist)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

    filename = 'chapterslist_data.json'
    with open(filename, 'w') as file:
        json.dump(validated_data.model_dump(), file)

    logger.info('New chapter list saved successfully.')
    return {'message': 'Data saved successfully'}


@router.get('/read_chapters/')
async def read_chapters():
    try:
        filename = 'chapterslist_data.json'
        with open(filename, 'r') as file:
            saved_data = json.load(file)
    except FileNotFoundError:
        logger.error('Chapter list data does not found')
        raise HTTPException(status_code=404, detail='Data not found')

    logger.info('Reading the chapter list.')
    return saved_data

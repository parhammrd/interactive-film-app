from src.logs import logger

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from sqlmodel import Session, select
from . import schemas, models
from src.database import engine


router = APIRouter(prefix='/scenario', tags=['scenario'])


def return_scenario(session):
    statement = select(models.Scenario).where(models.Scenario.id == 1)
    results = session.exec(statement)
    return results.first()


@router.post('/save-chapters/')
async def save_chapters(chapterslist: schemas.ChapterList):
    try:
        validated_data = schemas.ChapterList.model_validate(chapterslist)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

    with Session(engine) as session:
        existed_scenario = return_scenario(session)
        if existed_scenario:
            existed_scenario.chapterlist = validated_data.model_dump()
            scenario = existed_scenario
            logger.info('Chapter list updated successfully.')
        else:
            scenario = models.Scenario(chapterlist=validated_data.model_dump())
            logger.info('New chapter list saved successfully.')

        session.add(scenario)
        session.commit()

    return {'message': 'Data saved successfully'}


@router.get('/read_chapters/')
async def read_chapters():
    with Session(engine) as session:
        existed_scenario = return_scenario(session)
        if existed_scenario:
            logger.info('Reading the chapter list.')
            return existed_scenario.chapterlist
        else:
            logger.error('Chapter list data does not found')
            raise HTTPException(status_code=404, detail='Data not found')

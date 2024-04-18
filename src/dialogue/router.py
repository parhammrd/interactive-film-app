from src.logs import logger

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from sqlmodel import Session
from . import schemas, models
from src.database import engine


router = APIRouter(tags=['users'])


@router.post('/dialogue/')
def capture_answer(userresponse: schemas.UserResponse):
    """
    Capture the user answer during the watching film and create
    specific scenario for the interactive-film
    """
    try:
        validated_data = schemas.UserResponse.model_validate(userresponse)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

    with Session(engine) as session:
        item = models.Dialogue(
            userid=validated_data.email,
            question=validated_data.question,
            answer=validated_data.answer,
        )
        session.add(item)
        session.commit()

    logger.info('User response listed successfully.')
    return {'message': 'User response listed successfully'}

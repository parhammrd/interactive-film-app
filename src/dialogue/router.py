from src.logs import logger

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from . import schemas


router = APIRouter(tags=['users'])


@router.post('/dialogue/')
async def capture_answer(userresponse: schemas.UserResponse):
    """
    Capture the user answer during the watching film and create
    specific scenario for the interactive-film
    """
    try:
        validated_data = schemas.UserResponse.model_validate(userresponse)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

    print(validated_data.model_dump())

    logger.info('User response listed successfully.')
    return {'message': 'User response listed successfully'}

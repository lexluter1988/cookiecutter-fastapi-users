from fastapi import APIRouter, Depends

from app.auth.db import User
from app.auth.logic import current_active_user

test_app_router = APIRouter(prefix='/test-app')


@test_app_router.get('/welcome')
async def welcome(user: User = Depends(current_active_user)):  # noqa: B008
    return {f'Wilkomen {user.email}!'}

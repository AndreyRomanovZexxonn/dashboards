from typing import TYPE_CHECKING

from fastapi import APIRouter

if TYPE_CHECKING:
    pass


def build_main_router() -> APIRouter:
    api_router = APIRouter()
    return api_router

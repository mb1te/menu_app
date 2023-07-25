from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from src.api import router as api_router
from src.exceptions import NotFound
from src.settings import get_settings

settings = get_settings()
app = FastAPI(debug=settings.fastapi_debug)
app.include_router(api_router)


@app.exception_handler(NotFound)
async def catch_not_found(_, error: NotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=dict(detail=f"{error.entity} not found"),
    )

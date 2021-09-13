from typing import TYPE_CHECKING, Optional

from fastapi import FastAPI
from pywebio.output import put_text
from pywebio.platform.fastapi import asgi_app

from app.api import build_main_router
from app.utils.logs import init_logging

init_logging()


if TYPE_CHECKING:
    from typing import Mapping

app: FastAPI = FastAPI()
subapp = asgi_app(lambda: put_text('hello from pywebio'))
app.mount('/pywebio', subapp)


def add_middlewares(application: FastAPI, config: Optional['Mapping']):
    pass


@app.on_event('startup')
async def startup():
    add_middlewares(app, config=None)
    app.include_router(build_main_router())


@app.on_event('shutdown')
async def stop():
    pass


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        'app.main:app',
        port=8000,
        reload=True,
        debug=False,
        log_config=None
    )

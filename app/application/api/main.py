from fastapi import FastAPI 

from application.api.lists.task_handlers import router as task_router
from application.api.lists.user_handlers import router as user_router

def create_app() -> FastAPI:
    app =  FastAPI(
        title='Simple Kafka Chat',
        docs_url='/api/docs',
        description='A simple kafka + ddd example',
        debug=True,
    )
    app.include_router(task_router,prefix='/task')
    app.include_router(user_router,prefix='/user')
    return app
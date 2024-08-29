from fastapi import FastAPI 

from application.api.lists.handlers import router as task_router

def create_app() -> FastAPI:
    app =  FastAPI(
        title='Simple Kafka Chat',
        docs_url='/api/docs',
        description='A simple kafka + ddd example',
        debug=True,
    )
    app.include_router(task_router,prefix='/task')
    return app
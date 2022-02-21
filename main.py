from fastapi import FastAPI

from src.api.v1_apis import v1_api_router

app = FastAPI(
    title='云堇',
    description='ツイッタースクレイピングAPI',
    openapi_url='/yunjin/openapi.json',
    docs_url='/yunjin/docs'
)

app.include_router(v1_api_router, prefix=f'/yunjin/api')

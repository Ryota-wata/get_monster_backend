from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import task, done

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)


# CORSミドルウェアを設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのオリジンからのリクエストを許可
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのヘッダーを許可
)

# サンプルデータ
# data = {"message": "理解した"}

# @app.get("/api/data")
# def get_data():
#     return data

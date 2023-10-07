from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import monster

app = FastAPI()
app.include_router(monster.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ここに許可するオリジンを指定することができます。"*"はすべてのオリジンを許可しますが、セキュリティ上の懸念があるため、本番環境では特定のオリジンを許可するようにしてください。
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可します。安全な設定に合わせて制限を追加してください。
    allow_headers=["*"],  # すべてのヘッダーを許可します。必要に応じて制限を設定してください。
)

posts_db = []

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

@app.get("/ping")
def ping():
    return Response(content="pong", media_type="text/plain", status_code=200)
from fastapi import FastAPI
from typing import Optional
import uvicorn
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def home(limit = 10, published : Optional[bool] = False):
    if published:
        return {'details':f'{limit} published number of blogs'}
    else:
        return {'details':f'{limit} all number of blogs'}


# dynamic path
@app.get('/blog/{id}')
def blog(id : int, limit=10):
    # fetch blog with id = id
    return {'blog id = ':f'limit is : {limit} and id is: {id}'}

@app.get('/blog/{id}/comments')
def blog(id : int):
    return {'blog comments = ': {'1', '2', '3'}, "id of the comment is :" : id}

class Blog(BaseModel):
    title: str
    body: str
    name: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'Blog details':{f'tilte of blog is: {blog.title}\n', f'Body of the blog contains: {blog.body}\n', f'Name of the blog is: {blog.name}\n', f'is my blog published: {blog.published}'}}


if __name__ == "__main__":
    uvicorn.run(app, debug=True, host="localhost", port=5555)
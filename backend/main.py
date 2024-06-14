from fastapi import FastAPI, HTTPException
from logging_config import LoggerSetup
import logging

from pydantic import BaseModel

# Cria um logger raiz
logger_setup = LoggerSetup()

# Adiciona o logger para o módulo
logger = logging.getLogger(__name__)

app = FastAPI()

blog_posts = []


class BlogPost:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def __str__(self) -> str:
        return f"{self.id} - {self.title} - {self.content}"

    def toJson(self):
        return {"id": self.id, "title": self.title, "content": self.content}


class CreatePost(BaseModel):
    id: int
    title: str
    content: str


@app.post("/blog")
def create_blog_post(post: CreatePost):
    logger.warning(f"Creating post with title {post.title}")
    try:
        blog_posts.append(BlogPost(post.id, post.title, post.content))
        return {"status": "sucess"}
    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/blog")
def get_blog_posts():
    logger.warning("Getting all posts")
    return {"posts": [blog.toJson() for blog in blog_posts]}


@app.get("/blog/{id}")
def get_blog_post(id: int):
    logger.warning(f"Getting post with id {id}")
    for post in blog_posts:
        if post.id == id:
            return {"post": post.__dict__}
    raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/blog/{id}")
def delete_blog_post(id: int):
    logger.warning(f"Deleting post with id {id}")
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            return {"status": "sucess"}
    raise HTTPException(status_code=404, detail="Post not found")


class UpdatePost(BaseModel):
    title: str
    content: str


@app.put("/blog/{id}")
def update_blog_post(id: int, data: UpdatePost):
    logger.warning(f"Updating post with id {id}")
    try:
        for post in blog_posts:
            if post.id == id:
                post.title = data.title
                post.content = data.content
                return {"status": "sucess"}
        raise HTTPException(status_code=404, detail="Post not found")
    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

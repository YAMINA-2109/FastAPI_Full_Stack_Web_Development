from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from schemas.blog import CreateBlog, UpdateBlog
from db.models.blog import Blog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int):
    blog = Blog(
        title = blog.title,
        slug = blog.slug,
        content = blog.content,
        author_id = author_id
    )
    db.add(blog)
    try:
        db.commit()
        db.refresh(blog)
        return blog
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Error! Please, tray again..",
        )
    
def modifay_blog(id:int, new_blog: UpdateBlog, db: Session, author_id: int):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db :
        return {"error": f"Blog with id {id} does not existe!"}
    if not blog_in_db.author_id == author_id:
        return {"error": "Only the author can modify the blog!"}
    blog_in_db.title = new_blog.title
    blog_in_db.slug = new_blog.slug
    blog_in_db.content = new_blog.content
    blog_in_db.author_id = author_id

    db.commit()
    db.refresh(blog_in_db)
    return blog_in_db


def get_one_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def get_all_blogs(db: Session):
    blogs = db.query(Blog).all()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No blogs found"
        )
    return blogs

def retrive_active_blogs(db: Session):
    active_blogs = db.query(Blog).filter(Blog.is_active).all()
    if not active_blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No active blogs found"
        )
    return active_blogs

def delete_blog(id:int, db:Session, author_id:int):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog:
        return {"error": "Could not find the blog"}
    
    if not blog.first().author_id == author_id:
        return {"error": "Only the author can delete a blog"}
    blog.delete()
    db.commit()
    return {"msg":"Blog deleted succesfuly"}


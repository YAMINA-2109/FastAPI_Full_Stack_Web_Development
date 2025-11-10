from fastapi import Depends, APIRouter, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog
from db.models.user import User
from apis.v1.route_login import get_current_user
from db.repository.blog import create_new_blog, get_one_blog, get_all_blogs, retrive_active_blogs, modifay_blog, delete_blog

router = APIRouter()


@router.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session=Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog

@router.get("/blogs", response_model=List[ShowBlog], status_code=status.HTTP_200_OK)
def get_blogs(db:Session = Depends(get_db)):
    blogs = get_all_blogs(db=db)
    return blogs

@router.get("/active_blogs", response_model=List[ShowBlog], status_code=status.HTTP_200_OK)
def get_active_blogs(db:Session = Depends(get_db)):
    active_blogs = retrive_active_blogs(db)
    return active_blogs

@router.put("/{id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
def update_blog(id:int, new_blog: UpdateBlog, db: Session=Depends(get_db), current_user: User= Depends(get_current_user)):
    updated_blog = modifay_blog(id=id, new_blog=new_blog, db=db, author_id=current_user.id)
    if isinstance(updated_blog, dict):
        raise HTTPException(
            detail=updated_blog.get("error"),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    if not updated_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog does not exist")
    return updated_blog

@router.get("/{id}", response_model= ShowBlog, status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = get_one_blog(id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog does not exist")
    return blog

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_a_blog(id:int, db: Session = Depends(get_db), current_user: User= Depends(get_current_user)):
    msg = delete_blog(id=id, db=db, author_id=current_user.id)
    if msg.get("error"):
        raise HTTPException(
            detail=msg.get("error"),
            status_code=status.HTTP_400_BAD_REQUEST
        )

    return {"msg": msg.get("msg")}

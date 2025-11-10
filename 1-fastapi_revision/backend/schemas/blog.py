from typing import Optional
from pydantic import BaseModel, model_validator, ConfigDict
from datetime import datetime

class CreateBlog(BaseModel):
    title: str 
    slug: str
    content: Optional[str] = None

    @model_validator(mode='after')
    def generate_slug(self):
        if self.title:
            self.slug=self.title.replace(" ", "-").lower()
        return self

class UpdateBlog(CreateBlog):
    pass

class ShowBlog(BaseModel):
    title: str 
    content: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
        
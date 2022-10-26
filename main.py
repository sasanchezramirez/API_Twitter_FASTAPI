from datetime import date, datetime
from uuid import UUID
from typing import Optional, list

# Pydantic

from pydantic import BaseModel, EmailStr, Field

# Fastapi

from fastapi import FastAPI, status

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=25
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=25
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=25
    )
    birth_date: Optional[date] = Field(default=None)

class Tweet():
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Path Operations

@app.get(
    path="/"
)
def home():
    return {"twitter_APi" : "it works"}

## Users

@app.post(
    path = "/signup",
    response_model = User,
    status_code = status.HTTP_201_CREATED,
    summary = "Register a user",
    tags= ["Users"]
 )
def signup():
    pass

@app.post(
    path = "/login",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Login a user",
    tags= ["Users"]
 )
def login():
    pass

@app.get(
    path = "/users",
    response_model = list[User],
    status_code = status.HTTP_200_OK,
    summary = "Show all users",
    tags= ["Users"]
 )
def show_all_users():
    pass

@app.get(
    path = "/users/{user_id}",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Show a user",
    tags= ["Users"]
 )
def show_a_user():
    pass

@app.delete(
    path = "/users/{user_id}/delete",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Delete a user",
    tags= ["Users"]
 )
def delete_a_user():
    pass

@app.put(
    path = "/users/{user_id}/update",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "update a user",
    tags= ["Users"]
 )
def update_a_user():
    pass
## Tweets
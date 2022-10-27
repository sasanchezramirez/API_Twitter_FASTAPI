from datetime import date, datetime
from unittest import result
from uuid import UUID
from typing import Optional, List
import json

# Pydantic

from pydantic import BaseModel, EmailStr, Field

# Fastapi

from fastapi import Body, FastAPI, status

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

class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=25
    )

class Tweet(BaseModel):
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

## Users

### Register a user
@app.post(
    path = "/signup",
    response_model = User,
    status_code = status.HTTP_201_CREATED,
    summary = "Register a user",
    tags= ["Users"]
 )
def signup(user: UserRegister = Body(...)):
    """
    # SignUp

    This path operation registers a user in the app

    ## Parameters:
    - Request body parameter.
        - user: UserRegister
    
    Returns a JSON with the basic user information:
    - user_ide: UUD
    - email: Emailstr
    - first_name: str
    - last_name: str
    - birth_date: date
    """
    with open("users.json", "r+", encoding="utf-8") as f: 
            results = json.loads(f.read())
            user_dict = user.dict()
            user_dict["user_id"] = str(user_dict["user_id"])
            user_dict["birth_date"] = str(user_dict["birth_date"])
            results.append(user_dict)
            f.seek(0)
            f.write(json.dumps(results))
            return user

### Login a user
@app.post(
    path = "/login",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Login a user",
    tags= ["Users"]
 )
def login():
    pass

### Show all users
@app.get(
    path = "/users",
    response_model = List[User],
    status_code = status.HTTP_200_OK,
    summary = "Show all users",
    tags= ["Users"]
 )
def show_all_users():
    """
    This path shows all users in the app

    ## Parameters:
    -

    Returns a json list with all useres in the app:
    - user_ide: UUD
    - email: Emailstr
    - first_name: str
    - last_name: str
    - birth_date: date
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

### Show a user
@app.get(
    path = "/users/{user_id}",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Show a user",
    tags= ["Users"]
 )
def show_a_user():
    pass

### Delete a user
@app.delete(
    path = "/users/{user_id}/delete",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Delete a user",
    tags= ["Users"]
 )
def delete_a_user():
    pass

### Update a user
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

### Show all tweets
@app.get(   
    path = "/",
    response_model = List[Tweet],
    status_code = status.HTTP_200_OK,
    summary = "Show all tweets",
    tags = ["Tweets"]
)
def home():
    return {"twitter_APi" : "it works"}

### Post a tweet
@app.post(
    path = "/post",
    response_model = Tweet,
    status_code = status.HTTP_201_CREATED,
    summary = "Post a tweet",
    tags= ["Tweets"]
 )
def post_a_tweet():
    pass  

### Show a tweet
@app.get(
    path = "/tweets/{tweet_id}",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "Show a tweet",
    tags= ["Tweets"]
 )
def show_a_tweet():
    pass  

### Delete a tweet
@app.delete(
    path = "/tweets/{tweet_id}/delete",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "Delete a tweet",
    tags= ["Tweets"]
 )
def delte_a_tweet():
    pass  

### Delete a tweet
@app.put(
    path = "/tweets/{tweet_id}/update",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "Update a tweet",
    tags= ["Tweets"]
 )
def update_a_tweet():
    pass  
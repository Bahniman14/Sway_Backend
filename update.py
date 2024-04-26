from fastapi import FastAPI, Depends
from pydantic import BaseModel
from datetime import date, time
from App import app
from database import create_poll, create_channel, create_profile, upvote, downvote, comment, edit_profile, follow, sway, subscribe_channel, comment_like, comment_dislike
# (import all the functions), call them in different post methods 
from connection import conn


class CreatePoll(BaseModel):
    user_id: str
    poll_id: str
    question: str
    option_id1: str
    option_id2: str
    option_id3: str
    option_id4: str
    option1: str
    option2: str
    option3: str
    option4: str
    tag: str
    created_date: date
    created_time: time

class CreateChannel(BaseModel):
    user_id: str
    channel_name: str
    channel_id: str

class CreateProfile(BaseModel):
    user_id: str
    username: str
    photoURL: str
    about_me: str

class UpVote(BaseModel):
    poll_id: str

class DownVote(BaseModel):
    poll_id: str

class Comment(BaseModel):
    user_id: str
    poll_id: str
    comment_id: str
    comment: str
class Edit_Profile(BaseModel):
    user_id: str
    username: str
    visibility: bool
    photoURL: str
    about_me: str

class Follow(BaseModel):
    user_id1: str
    user_id2: str

class Sway(BaseModel):
    poll_id: str
    option_id: str

class SubscribeChannel(BaseModel): #Change area
    user_id: str
    channel_id: str #Change area

class CommentLike(BaseModel):
    comment_id: str
    user_id: str
class CommentDislike(BaseModel):
    comment_id: str
    user_id: str

# 1.
@app.post("/Create_Poll")
async def Create_Poll(create_poll_input: CreatePoll):
    print(create_poll_input)
    create_poll(conn, create_poll_input)
# 2.
# @app.post("/Create_Channel") 
# async def Create_Channel(create_channel_input: CreateChannel, conn = Depends(create_connection)):  #Change area
#     create_channel(conn, create_channel_input)
# 3.
@app.post("/Create_Profile") 
async def Create_Profile(create_profile_input: CreateProfile):  #Change area
   create_profile(conn, create_profile_input)
# 4.
# @app.post("/UpVote") 
# async def Up_Vote(upvote_input: UpVote, conn = Depends(create_connection)):  #Change area
#     upvote(conn, upvote_input)

# 5.
# @app.post("/DownVote") 
# async def Down_Vote(downvote_input: DownVote, conn = Depends(create_connection)):  #Change area
#     downvote(conn, downvote_input)

# 6.
# @app.post("/Comment") 
# async def Comment(comment_input: Comment, conn = Depends(create_connection)):  #Change area
#     comment(conn, comment_input)
# 7.
@app.post("/Edit_Profile") 
async def Edit_Profile(edit_profile_input: Edit_Profile):  #Change area
    edit_profile(conn, edit_profile_input)
# 8.
# @app.post("/Follow") 
# async def Edit_Profile(follow_input: Follow, conn = Depends(create_connection)):  #Change area
#     follow(conn, follow_input)
# 9
@app.post("/Sway") 
async def Sway(sway_input: Sway):
    sway(conn, sway_input)

# 10.
# @app.post("/Subsribe_Channel") 
# async def Subscribe_Channel(subscribe_channel_input: SubscribeChannel, conn = Depends(create_connection)):  #Change area
#     subscribe_channel(conn, subscribe_channel_input)
# 11.
# @app.post("/Comment_Like")
# async def Comment_Like(comment_like_input: CommentLike, conn = Depends(create_connection)):
#     comment_like(conn, comment_like_input)
# # 12.
# @app.post("/Comment_Dislike")
# async def Comment_Dislike(comment_dislike_input: CommentDislike, conn = Depends(create_connection)):
#     comment_dislike(conn, comment_dislike_input)

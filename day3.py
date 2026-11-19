import asyncio
from fastapi import FastAPI
from fastapi import Path

app = FastAPI()
@app.get('/users/hello')
async def get():
    return {"msg":"我正在学习fastapi"}
@app.get('/chat')
async def get2():
    return {"msg":"你好，我是一个聊天机器人"}
@app.get('/')
async def get3():
    return {"msg":"欢迎来到我的网站"}
@app.get('/users/{user_id}')
async def get4(user_id: int = Path(..., gt=0, lt=101, description="用户名在1-100之间")):
    return { "msg": "普通用户", "user_id": user_id }
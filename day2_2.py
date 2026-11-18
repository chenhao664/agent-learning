from fastapi import FastAPI

app = FastAPI()

# 临时用户数据
users = [
    {"id": 1, "name": "张三", "age": 20},
    {"id": 2, "name": "李四", "age": 25}
]

# GET：获取所有用户
@app.get("/api/users")
def get_users():
    return {
        "code": 0,
        "data": users
    }

# GET：获取指定用户
@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {
                "code": 0,
                "data": user
            }

    return {
        "code": 404,
        "message": "用户不存在"
    }
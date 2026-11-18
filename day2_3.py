import asyncio
import httpx

# 定义异步请求函数
async def get_data():

    # 创建异步 HTTP 客户端
    async with httpx.AsyncClient() as client:

        # 发送 GET 请求
        response = await client.get(
            "https://www.example.org/"
        )

        # 查看响应状态码
        print("状态码：", response.status_code)

        # 查看响应头
        print("响应头：", response.headers)

        # 查看网页内容
        print("网页内容：", response.text)


# 运行异步程序
asyncio.run(get_data())
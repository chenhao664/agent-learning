import httpx

# 访问网站
r = httpx.get('https://www.example.org/')

# 查看请求结果
print(r)

# 查看 HTTP 状态码
print(r.status_code)

# 查看网页内容类型
print(r.headers['content-type'])

# 查看网页 HTML 源代码
print(r.text)
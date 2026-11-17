import asyncio
import time

async def say_after(delay,what):
    await asyncio.sleep(delay)
    return f"{what}-{delay}"
    
async def main():
    start = time.perf_counter()
    print(f"started at {time.strftime('%x')}")
    ret = await asyncio.gather(
        say_after(1,'1'),
        say_after(1,'2'),
        say_after(1,'3'),
        say_after(1,'4'),
        say_after(1,'5')
    )
    print(ret)
    end = time.perf_counter()
    print(f"finished at {time.strftime('%x')}")
    print(f"总执行时间：{end - start:.2f} 秒")
asyncio.run(main())

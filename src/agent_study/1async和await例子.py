import asyncio

async def make_tea(name, seconds):
    print(f"开始做 {name}")
    await asyncio.sleep(seconds)  # 模拟等待，不阻塞别人
    print(f"{name} 做好了")
    return name

async def main():
    # 同时点三杯奶茶，总耗时约等于最慢的那杯
    await asyncio.gather(
        make_tea("珍珠奶茶", 2),
        make_tea("柠檬茶", 1),
        make_tea("美式咖啡", 3),
    )

asyncio.run(main())
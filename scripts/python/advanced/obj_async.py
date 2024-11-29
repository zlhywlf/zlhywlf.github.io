async def func1():
    print("func")
    return 1


async def main1():
    r = await func1()
    print("main")
    return r


m = main1()
try:
    m.send(None)
except StopIteration as e:
    print(e.value)  # 👉 1


def func2():
    print("func2")
    r = yield
    print(r)
    return 2


def main2():
    r = yield from func2()
    print("main2")
    return r


m = main2()

try:
    m.send(None)
    m.send("msg to func2")
except StopIteration as e:
    print(e.value)  # 👉 2

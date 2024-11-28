class Foo:

    def __getattr__(self, item):
        return "i am foo"

    def __getattribute__(self, item):
        print("call", end=": ")
        raise AttributeError


foo = Foo()
print(foo.unknown)  # 未定义属性 👉 call: i am foo

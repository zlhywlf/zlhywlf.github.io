class Foo:
    def __init__(self):
        self.lst = [1, 2, 3, 4]

    def __getitem__(self, item):
        return self.lst[item]


foo = Foo()
for f in foo:  # __getitem__
    print(f)
# 👆 等价于 👇
for f in foo.lst:
    print(f)

print(foo[::2])  # 支持切片 👉 [1, 3]

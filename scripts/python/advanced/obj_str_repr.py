class Foo:

    def __str__(self):
        return "i am foo"

    def __repr__(self):
        return "I AM FOO"


foo = Foo()
print(foo)  # 👉 i am foo
print(repr(foo))  # 👉 I AM FOO

class Foo:
    pass


class Bar(Foo):
    pass


foo = Foo()
age = 18
print(f"整型常量的类型: {type(18)}")  # noqa:  UP003 👉 <class 'int'>
print(f"整数类型的类型: {type(int)}")  # 👉 <class 'type'>
print(f"整型变量的类型: {type(age)}")  # 👉 <class 'int'>
print(f"Foo实例的类型: {type(foo)}")  # 👉 <class '__main__.Foo'>
print(f"Foo自身的类型: {type(Foo)}")  # 👉 <class 'type'>
print(f"type类的类型: {type(type)}")  # 👉 <class 'type'>
print(f"object的类型: {type(object)}")  # 👉 <class 'type'>

print(f"整数类型的父类: {int.__bases__}")  # 👉 (<class 'object'>,)
print(f"Foo自身的父类: {Foo.__bases__}")  # 👉 (<class 'object'>,)
print(f"Bar自身的父类: {Bar.__bases__}")  # 👉 (<class '__main__.Foo'>,)
print(f"type类的父类: {type.__bases__}")  # 👉 (<class 'object'>,)
print(f"object的父类: {object.__bases__}")  # 👉 ()

print(f"type 是 type 的实例: {isinstance(type, type)}")  # 👉 True
print(f"object 是 type 的实例: {isinstance(object, type)}")  # 👉 True

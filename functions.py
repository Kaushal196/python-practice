# def hello_func():
#     pass               #if we want to create an empty fun

# print(hello_func)       #op <function hello_func at 0x0000021712067F70>


# def hello_World():
#     print("Hello World")

# hello_World()  
# #op-> Hello World

def test_fun(*args, **kwargs):
    print(type(args))
    print(args)
    print(kwargs)

test_fun('Math', 1,  2, name="kp", age="23")

#op->
# <class 'tuple'>
# ('Math', 1, 2)
# {'name': 'kp', 'age': '23'}








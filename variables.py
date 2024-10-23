a = 1

b = str(a)
c = float(a)

print(type(a), a)
print(type(b), b)
print(type(c), c)

x, y, z = 'a', 'b', 'c'
print(x, y, z)

x = y = z = 'one value to many'
print(x, y, z)

arch = ['gothic', 'classic', 'postmodernism']
x, y, z = arch
print(x, y, z)

# ERROR CASE int + str = a + b

a = 'global a'

def fn():
    a = 'local a'
    print('fn', a)


print('global', a)
fn()


def fn_with_global_var():
    global a
    a = 'global defined within fn scope'


fn_with_global_var()
print(a)

x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
x = {"name": "John", "age": 36}
print(x["name"])
x = {"apple", "banana", "cherry"}












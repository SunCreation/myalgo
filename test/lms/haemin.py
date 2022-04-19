number = 237
m = [1,1,2,3,5,8,13,21,34,55,89,144,233]

def f(i):
    global number; number -= i
    return i

result = [f(i) for i in reversed(m) if number >= i]

print(result)
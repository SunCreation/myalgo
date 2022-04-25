A, B, V = map(int, input().split())

count = 0
V -= A
num, V= V//(A-B), V%(A-B)
V += A
while True:
    V -= A
    count += 1
    if V <= 0: break
    V += B
print(count+num)
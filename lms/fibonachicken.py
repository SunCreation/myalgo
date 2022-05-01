people = int(input('몇명을 먹일까요? :'))

RATIO = 1/2 + (5**0.5)/2

def fibo_chicken(num):
    print(abs(num/(i:=int(num/RATIO)) - RATIO), abs(num/(i+1) - RATIO))
    return i if abs(num/(i:=round(num/RATIO)) - RATIO) < abs(num/(i+1) - RATIO) else i + 1

print(f'{fibo_chicken(people)}마리 치킨이 필요합니다.')
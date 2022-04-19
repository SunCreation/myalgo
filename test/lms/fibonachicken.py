people = int(input('몇명을 먹일까요? :'))

RATIO = 1/2 + (5**0.5)/2

def fibo_chicken(num):
    return round(num/RATIO)

print(f'{fibo_chicken(people)}마리 치킨이 필요합니다.')
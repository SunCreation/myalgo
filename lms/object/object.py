
# Everything in Python is an object, and almost everything has attributes and methods.
#%%
class Car:
    pass

class Car():
    pass

#id(Car)는 여러번 호출해도 같은 값이 얻어집니다. 
print(id(Car))
print(id(Car))

#id(Car())는 Car()가 호출될 때마다 다른 값이 얻어집니다. 
print(id(Car()))
print(id(Car()))

# 두 객체의 type을 살펴봅니다. 
print(type(Car))
print(type(Car()))
print(type(int()))
# %%
mycar = Car()
mycar2 = Car()
print(id(mycar))
print(id(mycar2))
# # %%
# # Car 클래스입니다.
# class Car:
#     '''
#     속성은 클래스의 상태를 나타냅니다.
#     색상: 빨강
#     종류: 스포츠 카
#     '''
#     color = 'red'
#     category = 'sports car'
		
#     '''
#     동작은 메서드로 나타냅니다.
#     '''
#     def drive(self):
#     '''
#     주행 메서드
#     '''
#         print("I'm driving")
				
#     def accel(self, speed_up, current_speed=10):
#     '''
#     가속 메서드
#     :param speed_up: 현재속도
#     :param current_speed: 가속
#     :type speed_up: string
#     :type current_speed: string
#     '''
#         self.speed_up = speed_up
#         self.current_speed = current_speed + speed_up
#         print("speed up", self.speed_up, "driving at", self.current_speed)

#%%
class Car:
    color = 'red'
    category = 'sports car'

    def drive(self):
        print("I'm driving")

    def accel(self, speed_up, current_speed=10):
        self.speed_up = speed_up
        self.current_speed = current_speed + speed_up
        print("speed up", self.speed_up, "driving at", self.current_speed)
mycar = Car()
mycar.drive()
Car.drive(mycar)
# %%
class Test:
    def run1(self):
        print("run1")
        print(self)

    def run2():
        print("run2")

t = Test()
t.run1()
t.run2()
# %%
class Test2:
    def run1(self, a):
        self.a = float(a) * 10
        print(self.a)

    def run2(self, b):
        b = float(b) + 10
        print(self.b)
        
t = Test2()

t.run1(1)
t.run2(1)
# %%
class Car:
    color = 'red'
    category = 'sports car'

    def drive(self):
        print("I'm driving")

    def accel(self, speed_up, current_speed=10):
        self.speed_up = speed_up
        self.current_speed = current_speed + self.speed_up
        print("speed up", self.speed_up, "driving at", self.current_speed)
# 아래처럼 수정해야, 속성값이 초기화되면서 객체를 생성할 수 있다.
class Car2:
    # def __init__(self, color, category):
    #     self.color = color
    #     self.category = category
    def __init__(self, color='red', category='sprots car'):
        self.color = color
        self.category = category

    def drive(self):
        print("I'm driving")

    def accel(self, speed_up, current_speed=10):
        self.speed_up = speed_up
        self.current_speed = current_speed + self.speed_up
        print("speed up", self.speed_up, "driving at", self.current_speed)


car1 = Car()
car2 = Car2('yellow', 'sedan')
print(car1.color)
print(car2.color)
print(car1.category)
print(car2.category)

# %%
# 인스턴스와 클래스에서 __dict__ 속성을 출력해보면 현재 인스턴스와 클래스의 속성을 딕셔너리로 확인할 수 있습니다.
# class 클래스이름:
#    __속성 = 값    # 비공개 클래스 속성
# 함수와 마찬가지로 클래스와 메서드도 독스트링을 사용할 수 있습니다. 다음과 같이 클래스와 메서드를 만들 때 
# :(콜론) 바로 다음 줄에 """ """(큰따옴표 세 개) 또는 ''' '''(작은따옴표 세 개)로 문자열을 입력하면 됩니다. 
# 그리고 클래스의 독스트링은 클래스.__doc__ 형식으로 사용하고, 메서드의 독스트링은 클래스.메서드.__doc__ 또는 
# 인스턴스.메서드.__doc__ 형식으로 사용합니다.

# class Person:
#     '''사람 클래스입니다.'''
    
#     def greeting(self):
#         '''인사 메서드입니다.'''
#         print('Hello')
 
# print(Person.__doc__)             # 사람 클래스입니다.
# print(Person.greeting.__doc__)    # 인사 메서드입니다.
 
# maria = Person()
# print(maria.greeting.__doc__)     # 인사 메서드입니다.
class Car:
    Manufacture = "India"

    def __init__(self, color='red', category='sedan'):
        self.color = color
        self.category = category

    def drive(self):
        print("I'm driving")

    def accel(self, speed_up, current_speed=10):
        self.speed_up = speed_up
        self.current_speed = current_speed + self.speed_up
        print("speed up", self.speed_up, "driving at", self.current_speed)

class NewCar(Car):
    def __init__(self, maker, color='Green', category='car'):
        super().__init__(color, category)
        self.maker = maker

    def fly(self):
        print("I'm flying!! This is the new car!!")

    def accel(self, speed_up, level=1, current_speed=10):
        self.boost[level] = {1 : 0, 2 : 30, 3 : 50}
        self.speed_up = speed_up + self.boost[level]
        self.current_speed = current_speed + self.speed_up
        print("speed up", self.speed_up, "driving at", self.current_speed)

mycar = NewCar('me')
print(mycar.color)
mycar.drive()
mycar.fly()

# %%
class FunnyDice:
    def __init__(self,n):
        self.plane=  n
    
    def play():
        pass
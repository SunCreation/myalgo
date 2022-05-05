def numbers():
    X=[]
    while True:
        number = input("Enter a number (<Enter key> to quit)") 
        while number !="":
            try:
                x = float(number)
                X.append(x)
            except ValueError:
                print('>>> NOT a number! Ignored..')
            number = input("Enter a number (<Enter key> to quit)")
        if len(X) > 1:
            return X

def median(nums): 
    nums.sort()
    size = len(nums)
    p = size // 2
    if size % 2 == 0:
        pr = p
        pl = p-1
        mid = float((nums[pl]+nums[pr])/2)
    else:
        mid = nums[p]
    return mid

def means(nums):
    total = 0.0
    for i in range(len(nums)):
        total = total + nums[i]
    return total / len(nums)

def std_dev(nums, avg):
   texp = 0.0
   for i in range(len(nums)):
       texp = texp + (nums[i] - avg) ** 2
   return (texp/len(nums)) ** 0.5

def main():
    X = numbers()
    med = median(X)
    avg = means(X)
    std = std_dev(X, avg)
    print("당신이 입력한 숫자{}의 ".format(X))
    print("중앙값은{}, 평균은{}, 표준편차는{}입니다.".format(med, avg, std))

if __name__ == '__main__':
    main()
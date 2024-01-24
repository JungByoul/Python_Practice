# # def hello():
# #     print('hello, word')
    
# # for _ in range(10):
# #     hello()
    
# def  add(x, y):
#     print(x + y)
# add(10, 30)

# x, y, z = list(map(int, input().split()))
# def inp(x, y, z):
    
#     return x*y*z

# print(inp(x, y, z))

# def add_sub(a, b):
#     return a + b, a - b
# x, y = add_sub (10, 20)
# print(x, y)


# def add_multi(al,b1, c1) :
#     return  al+b1+c1, al*b1*c1
# a,b,c= map(int, input("3개의 값 입력 ").split())

# result1, result2 = add_multi(a,b,c)
# print("합은 %d, 곱은 %d" %(result1, result2))
# print(f"합은 {result1}, 곱은 {result2}")


# x, y = 10, 3

# def get_quo_remain(a, b):
#     return a//b, a%b
# quo, rem = get_quo_remain(x, y)

# print(f"몫: {quo}, 나머지: {rem}")


def cal(x,y):
    def add(x,y):
        return x+y
    def minus(x,y):
        return x-y
    def multiple(x, y):
        return x*y
    def div(x,y):
        return x/y
    def rem(x,y):
        return x%y

def calc_fun(type,a,b) :
    if (type == 1):
        return a + b
    elif(type == 2):
        return a - b
    elif(type == 3):
        return a * b
    elif(type == 4):
        return a / b
    elif(type == 5):
        return a % b

while True:
    nCal = int(input("원하는 연산자를 입력하세요."))
    if nCal == 6:
        print("종료를 선택하셨습니다. 프로그램을 종료합니다..")
        break
    elif nCal > 0 and nCal <=5:
        nFir = int(input("첫번째 숫자를 입력하세요."))
        nSec = int(input("두번째 숫자를 입력하세요."))
        result = calc_fun(nCal, nFir, nSec)
        print(f"결과는 {result}입니다")        
    else:
        print("잘못 입력하였습니다. 다시 입력하세요")
        continue
        

def hello():
    print('hello, word')
    
for _ in range(10):
    hello()


def  add(x, y):
    print(x + y)
add(10, 30)


x, y, z = list(map(int, input().split()))
def inp(x, y, z):
    
    return x*y*z

print(inp(x, y, z))


#계산기 코드
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
        

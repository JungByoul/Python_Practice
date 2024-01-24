# # # x = int(input())
# # # if x == 7:
# # #     print('행운')

# # # x=10
# # # if x== 10:
# # #     pass

# # cash = int(input("값 입력"))
# # coupon = input("쿠폰 입력").split('h')
# # discount = int(coupon[-1])
# # print(cash - discount)



# # nInp = int(input())
# # if nInp %2 == 1:
# #     print('홀수')
# # else:
# #     print('짝수')

# # x = 10
# # y = 20
# # if x == 10 and y == 20:
# #     print('참')
# # else:
# #     print('거짓 ')
    
    
# # written_test = 75
# # coding_test = True

# # if written_test >= 80 and coding_test:
# #     print('합격')
# # else:
# #     print('불합격')


# kor, eng, mat, sci = list(map(int, input().split()))

# def range(x):
#     return 0 <= x and x <= 100

# if range(kor) and range(eng) and range(mat) and range(sci):
#     nAvg = (kor + eng + mat + sci)/ 4
#     if nAvg >= 80:
#         print('합격')
#     else:
#         print('불합격')
# else:
#     print('잘못된 점수')
    
# x = 30
# if x == 10:
#     print ('10입니다. ')
# elif x == 20:
#     print (' 20입니다. ')
# else:
#     print ('10도 20도 마닙니다. ')
    
# nData = int(input())

# if nData == 1:
#     print('콜라')
# elif nData == 2:
#     print('사이다')
# elif nData == 3:
#     print('환타')
# else:
#     print('제공하지 않는 메뉴')


# nStudent, nLevel = list(map(int, input().split()))

# if nStudent == 1:
#     if nLevel == 1:
#         print('학생이며 초등학생입니다')
#     elif nLevel == 2:
#         print('학생이며 중학생입니다')
#     elif nLevel== 3:
#         print('학생이며 고등학생입니다')
# else:
#     print('학생이 아닙니다')
    
# #자판기
# nMoney, nButton = list(map(int, input().split()))

# if nButton == 1:
#     print(600 - nMoney)
# elif nButton == 2:
#     print( - nMoney)
# elif nButton ==3:
#     print ( -nMoney)

# x = int(input())
# if x >=11 and x<= 20:
#     print('11~20')
# elif x>=21 and x<=30:
#     print('21~30')
# else:
#     print('아무것도 해당하지 않음')


# age = int(input())
# balance = 9000
# if age<= 12:
#     print(balance-650)
# elif age<= 18:
#     print(balance-1050)
# elif age>=19:
#     print(balance-1250)
# else:
#     print(balance)

# x,y = map(int, input().split())

# if x>0 and y>0:
#     print('제1사분면')
# elif x<0 and y>0:
#     print('제2사분면')
# elif x<0 and y<0:
#     print('제3사분면')
# elif x<0 and y<0:
#     print('제4사분면')
# else:
#     print('선 위에 위치함')
    

# x, y = list(map(int, input().split(",")))

# if (50<= x <=100) and (40<=y <=80):
#     print("사각형 안에 있습니다")
# else:
#     print("사각형 안에 없습니다")

# colors = ['red', 'white','black','orange', 'blue', 'dark blue', 'green','purple']
# strData =input()
# if strData in colors:
#     print("신규")
# else:
#     print("중복")

# x = int(input())
# if x+ 25 >255:
#     print(255)
# else:
#     print(x+25)


# nData = int(input())
# if nData<20:
#     print(0)
# else:
#     print(nData-20)

# print(nData)


# pixel = int(input("입력값:"))
# if pixel - 20 < 0:
#     pixel = 0
# elif pixel - 20 > 255 :
#     pixel = 255
# else :
#     pixel = pixel - 20
# print("출력값:", pixel)

# hh, mm = list(input().split(':'))
# if mm == '00':
#     print('정각입니다')
# else:
#     print('정각이 아닙니다')


# nAge = input()
# nRealAge = int(nAge[:2])

# if nRealAge >=15:
#     print('성년입니다')
# elif nRealAge <15:
#     print('미성년입니다')


# nId = input()
# if len(nId) != 7:
#     print('자릿수가 틀립니다')
# else:
#     if nId[0] == '1' or nId[0] == '3':
#         print('남자입니다')
#     elif nId[0] == '2' or nId[0] == '4':
#         print('여자입니다')


# nAge = input()
# nRealAge = int(nAge[0]+nAge[1])
# if 10 <= nRealAge <=18:
#     print('미성년입니다')
# elif 19 <= nRealAge <= 99:
#     print('성년입니다')
# else:
#     print('범위를 초과하였습니다')


# nMoney = int(input('금액을 입력하세요:'))
# nDrink = int(input("음료를 선택하세요:"))
# nResult = 0

# if nMoney <10000:
#   if nDrink == 1:
#      nResult = nMoney - 700
#   elif nDrink == 2:
#       nResult = nMoney - 600
#   elif nDrink ==3:
#       nResult = nMoney - 800
# else:
#     print("최대금액 초과")

# if nResult <0:
#     print("금액 부족")
# else:
#     print(nResult)



# for i in reversed(range(10)):
#     print(i)

# for i in range(1, 11, 1):
#     print(i, end=' ')

# nstart =int (input("시작 숫자를 입력하세요"))
# nend = int(input("끝 숫자를 입력하세요"))
# nInterval = int(input("간격을 입력하세요"))
# for i in range(nstart, nend + 1, nInterval):
#     print (i, end=' ')


# nstart = int(input("시작 숫자를 입력하세요!"))
# nend = int(input("끝 숫자를 입력하세요!"))
# nInterval = int(input("간격을 입력하세요!"))

# if (nInterval <0 and nstart < nend) or (nInterval >0 and nstart > nend):
#     print('입력된 내용이 적절하지 않습니다')

# else:
#     if nInterval >0 and nstart < nend:
#         for i in range(nstart, nend+1, nInterval):
#             print(i, end = ' ')
#     elif nInterval <0 and nstart > nend:
#         for i in range(nstart, nend-1, nInterval):
#             print(i, end = ' ')


# x = [49, -17, 25, 102, 8, 62, 21]

# for i in x:
#     print(i *10, end=' ')


# nInput = int(input())
# for j in range(10):
#     print(f"{nInput} * {j} = {j*nInput}")
    
# nInput = int(input())
# cnt = 0

# for i in range(nInput+1):
#     cnt += i
# print(cnt)


# cnt = 0
# for i in range(1, 11):
#     nWeight = float(input())
#     print(f"{i} 번쨰의 돌\n\t무게(g) : {nWeight}")
#     cnt+= nWeight
# print("평균 : ", cnt/nWeight, "g")

# cnt = 0
# for i in range(1, 11):
#     nWeight = float(input(f"{i} 번쨰의 돌\n\t무게(g) : "))
#     cnt+= nWeight
# print("평균 : ", cnt/nWeight, "g")


# nNum = int(input("학생의 수: "))
# nTotal = 0
# for i in range(1, nNum+1):
#     x = int(input(f"{i}번 학생의 점수: "))
#     nTotal += x
# print(f"평균\t: {nTotal/nNum}점")



# i = 0
# while i < 100:
#     print('Hello, world!')
#     i += 1

# x=1
# for _ in range(10):
#     print(x, end='  ')
#     x+=1

# y=1
# while y<11:
#     print(y, end='  ')
#     y+=1
    
# i=-50
# count = 1
# while i <= 1:
# if count%5 == 0:
# print(i, end = "It")
# print ()
# ere: , print (i,end = "It")
# i+=1
# count += 1


# i=-50
# count = 1
# while i <= 1:
#     print(i,end = "It")
# if count%5 == 0:
#     print ()
#     i+=1
#     count += 1
    


# nData = int(input("총합을 구할 숫자를 입력하세요 : "))
# nTotal = 0
# while nData > 0:
#     nTotal += nData # nTotal = nTotal + nData
#     nData -=1
# print('총합은 : ' nTotal)

# nData = int(input("총합을 구할 숫자를 입력하세요 :"))
# nTotal = 0
# for i in range(1, nData+1) :
#     nTotal += i
# print('총합은 : ', nTotal)


# Kor = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

# total = 0
# count = 0
# index = 0

# while index < len(Kor):
#     total += Kor[index]
#     count += 1
#     index += 1

# average = total / count
# print(f"A 학급의 평균 점수는 {average:.2f}입니다.")


# result = 1
# power = 0

# while power < 20:
#     result *= 2
#     power += 1

# print(f"2의 20승은 {result}입니다.")


# nYear = int(input())
    
# if nYear % 400 == 0:
#     print('윤년')
# elif nYear %4 == 0 and nYear % 100 != 0:
#     print('윤년')
# else:
#     print('평년')




import random

# idx = 0
# while idx <=100:
#     print(random.randrange(1,7))
#     idx +=1

# i=0
# cnt_rand = [0,0,0,0,0, 0]
# while i<1000:
#     value = random.randrange(1,7)

#     cnt_rand[value-1] += 1
#     i+= 1
    
# print (cnt_rand)

# nMoney = int(input("금액을 입력하세요!"))
# print("결과")
# while nMoney >0:
#     nMoney -=1350
#     if nMoney>0:
#         print(nMoney)



# total = 0
# i = 0
# while True:
#         i+=1
#         total +=i
#         if i == 100:
#             break
# print(total)


# nTimes = int(input())
# i =0
# while True:
#     print(i)
#     i+=1
#     if i ==nTimes:
#         break


# count = int(input())

# for i in range(count):
#     if i %2 == 0:
#         continue
#     print(i)


# i = 0
# while True:
#     if i %10 != 3:
#         i+= 1
#         continue
#     if i >73:
#         break
    
#     print(i, end=' ')
#     i +=1

# i = 0
# while True:
#     i += 1
#     if i % 10 != 3:
#         continue
    
#     if i>73:
#         break
#     print(i, end = ' ')



# for _ in range(5):
#     for _ in range(5):
#         print('*', end = '')
#     print()


# cnt = 0
# for i in range(5):
#     cnt += 1
#     for j in range(cnt):
#         print('*', end='')
#     print()


# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

#FizzBuzz 문제
# i = 0
# while True:
#     i += 1
#     if i >100:
#         break
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz', end =' ')
#     elif i % 5 == 0:
#         print('Buzz', end=' ')
#     else:
#         print(i, end=' ')


# 큰 틀에서 우선 앞의 논리 연산자를 충족하면 문자열을 출력하고,
# 그게 아니면 or 뒤에 있는 i 값을 출력한다.
# or 연산자의 특성상 앞의 값이 참이라면, 앞의 값만 출력하기 때문이다.

# 앞의 논리연산자들을 살펴보면, 괄호 안의 비교 연산자를 통해
# True 혹은 False의 값이 도출된다.
# 그리고 이 값들은 곱하기(*)를 통해 Fizz와 Bizz 각각을 출력하고,
# 두 조건(3의 배수, 5의 배수)가 공통적으로 일치하면
# FizzBizz를 같이 합쳐서 출력하는 것이다.

print(False or 1)

#True False는 연산하게 되면 1과 0이 된다!



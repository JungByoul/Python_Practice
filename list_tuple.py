#리스트 기초
a=[]
for i in range(10):
    a.append(i)


a=[]
for i in range(1, 11):
    a.append(i*10)


b=[]
for i in range(50):
    b.append((i+1)*2)

#22.1 리스트 조작하기
#리스트 안에 리스트 추가하기
a = [10, 20, 30]

a.insert(2, 500)

#리스트에서 특정 인덱스의 요소 삭제하기
a= [10, 20, 30]
a.pop(1)
a= [10, 20, 30]
del a[1]
print(a)

#pop과 for문을 사용해서 다음 list를 빈 리스트로 만들기
nList = [0,1,2,3,4,5]
for i in range(6):
    nList.pop(0)
print(nList)

#리스트에서 특정 값을 찾아 삭제하기
a = [10, 20, 30]
a.remove(30)

#리스트로 스택만들기
a=[]
a.append(10)
a.append(20)
a.append(30)
a.append(40)
print(a)
for _ in range(len(a)):
    a.pop()
print(a)


a = []
for i in range (4):
    i += 1
    a.append(i*10)
    print(a)
for i in range (4) :
    print(a.pop ())
    
    
a = [0, 0, 0, 0, 0]
b = a. copy ()

print(a is b)
print( b is a)


a = [10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]

target_value = 20
indices = []

for index, value in enumerate(a):
    if value == target_value:
        indices.append(index)

print(indices)


a = [38, 21, 53, 62, 19]
i = 0
while i < len(a):
    print(a[i])
    i += 1
    

val = a[0]
for elem in a:
    if elem < val:
        val = elem



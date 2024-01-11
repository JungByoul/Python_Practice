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



n, k = map(int, input().split())
nList = []
for i in range(1, n+1):
    nList.append(i)
ans=[]

idx = k-1 #0부터 시작하는 인덱스이므로 1빼는것
count = 1


for _ in range(n-1):
  ans.append(nList.pop(idx)) #이동해서 빼기
  
  idx = idx+k-1 #다음 인덱스로 이동
  
  if idx>=len(nList): #배열의 끝에 왔을 때.
    idx = idx%len(nList)

#이하 출력
print("<", end='')
for elem in ans:
    print(elem, end=', ')
    
print(nList[0], ">", sep="")

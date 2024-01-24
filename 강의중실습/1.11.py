# a= [10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]
# b=[]
# while 20 in a:
#    b.append(a.index(20))
#    a[a.index(20)]= 'x'
   


# a = [0, 0, 0, 0, 0]
# b = a. copy ()

# print(a is b)
# print( b is a)


# a = [38, 21, 53, 62, 19]

# val = a[0]
# for elem in a:
#     if elem < val:
#         val = elem
    

# a = [38,21,53, 62,19]
# max_data = a[0]
# min_data = a[0]
# for i in a:
#     if i > max_data:
#         max_data = 1
#     if i < min_data:
#         min_data = i
        
# print ("Max Data =", max_data, "Min Data =", min_data)


# numbers=[]
# for i in range(10):
#     numbers.append(i+1)

# for elem in numbers:
#     if elem %2 == 1:
#         numbers.pop(numbers.index(elem))
# print(numbers)
        

# x = [i for i in range(5, 15) if i % 2 == 0]
# print(x)


# nums = [i for i in range(1, 10) ]

# nums = [i * j for i in range(2, 10) for j in range(1,10)]
# print(nums)


# a = ['alpha', 'bravo', 'charlie' , 'delta', 'echo', 'foxtrot'
# , 'golf', 'hotel', 'india']

# b = [elem for elem in a if len(elem) == 5]
# print (b)


# x, y = list(map(int, input().split()))

# if (x < 1 or x > 20):
#     print ("1st data range error")
# elif (y < 10 or y > 30):
#     print ("2nd data range error")
# elif (x >= y):
#     print("Data input range error")
# else:
#     nums = [2**i for i in range(x, y+1)]
#     del nums[1]
#     del nums[len(nums) -2]
#     print(nums)



# ai_classes = {
#     'class01' : [
#                {'name' : '서준', 'age' : 24},
#                {'name' : '하준', 'age' : 34},
#                {'name' : '도윤', 'age' : 37},
#                {'name' : '시윤', 'age' : 19},
#                {'name' : '은우', 'age' : 31}
#     ],
#     'class02' : [
#                  {'name' : '지호', 'age' : 34},
#                  {'name' : '예준', 'age' : 19},
#                  {'name' : '동원', 'age' : 21},
#                  {'name' : '민정', 'age' : 22},
#                  {'name' : '효주', 'age' : 24}
#     ]
# }

# for class_num in ai_classes:
#     for i in range(5):
#         if ai_classes[class_num][i]['age']>=30:
#             print(ai_classes[class_num][i]['name'],':' , ai_classes[class_num][i]['age'] ,end=' / ')



# for classes in ai_classes:
#     print(classes[0])
#     for elem in classes:
#         print(elem)
        # if elem1['age'] >= 30:
            # print(elem1['name'] ,':', elem1['age'] )
        

# ai_classes['class01'][elem]


# a =[[10, 20], [30, 40], [50, 60]]
# for aa in a:
#     for aaa in aa:
#         print(aaa, end =' ')
#     print()
# for x, y in a:
#     print(x, y)


# a= []
# for i in range(3):
#     a.append([])
#     for j in range(2):
#         a[i].append(0)
# print(a)

# a = [[0]* i for i in range(3) for j in range(2)]

# print("I am %s, you? " %'fine')
# print("All thing is %.2f " %120.2)


# x, y = list(map(int, input().split()))
# print("%d + %d = %d 입니다" %(x, y, x+y))


# print("Hello {0} wow {1} {2}good".format(1, 'hello', 4.3))

# print("{0} {0} {1} {1}".format("python", "script"))
# print("%s %s %s %s %s %s" %("python", "python", "python", "script", "script", "script"))

# print("Hello, %s %s %f" %())

# a, b = map(int, input().split())
# t = a + b
# print('t)+ 4= 4 입니다'. format (a,b,t))


# language = "Python"
# version = 3.6

# print(f"hello, {language} verison {version}")



path = 'C:\\Users\\Edu\\AppData\\Local\\Programs\\Python\\Python36-32\\data.txt'
x=path.split('\\')
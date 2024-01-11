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


x, y = list(map(int, input().split()))

if (x < 1 or x > 20):
    print ("1st data range error")
elif (y < 10 or y > 30):
    print ("2nd data range error")
elif (x >= y):
    print("Data input range error")
else:
    nums = [2**i for i in range(x, y+1)]
    del nums[1]
    del nums[len(nums) -2]
    print(nums)


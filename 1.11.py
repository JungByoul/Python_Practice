# a= [10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]
# b=[]
# while 20 in a:
#    b.append(a.index(20))
#    a[a.index(20)]= 'x'
   


# a = [0, 0, 0, 0, 0]
# b = a. copy ()

# print(a is b)
# print( b is a)


a = [38, 21, 53, 62, 19]

val = a[0]
for elem in a:
    if elem < val:
        val = elem
    
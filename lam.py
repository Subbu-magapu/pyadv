#lambda

'''add = lambda x, y: x + y
print(add(10,26))'''


#map
'''''numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)'''''

#filter
''''nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x%2==0, nums))
print (evens)'''''

''''nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x %2 !=0, nums))
print (evens)'''''

#reduce
'''from functools import reduce
nums = [1 , 2, 3, 4, 5]
result =reduce(lambda x, y: x * y, nums)
print(result)'''
 
#even or odd
'''s= lambda x: "even" if x%2==0 else "odd"
print(s(3))'''

#prime 
'''s = lambda x: "not prime" if x%2==0 else "prime"
print(s(8))'''

#keyword
'''def add_number (*args):
    return sum(args)
print(add_number(1,2))
print(add_number(1,2,3,4,5,6))'''

#kargs(variable length arg)
'''def f (*marks):
    print(sum(marks))

f(80,20,30,40,50,60)'''

#kargs(variable len keyword argument)
'''def f (**marks):
    print(marks)

f(telugu=80 ,
  hindi=70,
  maths=90,
  social=100)'''

#expression inside 
'''x = 5
y = 3
print (f"{x} * {y} = {x*y}")'''

'''x = 5
y = 3
print (f"{x} / {y} = {x/y}")'''

'''x = 9
y = 91
print (f"{x} + {y} = {x+y}")'''

'''x = 100
y = 50
print (f"{x} - {y} = {x-y}")'''

'''x = 45
y = 4
print(f"{x} % {y} = {x%y}")'''






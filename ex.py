#1.
a = 181
print a
#2.
b = "james"
print b
#3.
c = 1.23
print c
#4.
print('Hello i am {} and i am {} years old!'.format(b,a))
#5.
x = 4
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
#print(x += y)
print(x%(y))
#6.
e = False
if not e:
    print('condition met')
else:
     print('condition not met')
     
if 1 < 2 and 4 > 2:
    print('condition met')
if 1 > 2 and 4 < 2:
    print('condtion not met')
if 4 < 9 or 8 > 3:
    print('condtion met')
#7
x = 1
if x == 10:
    print('10')
elif x == 9:
    print('9')
else:
    print('x is not 9 or 10')
#8 and 9
count = 0
while count == 0:
    count = count + 1
    print count
for count in range(5,10):
    print count
#10
list1 = [1,2,3,4,5]
for list1 in range(1,4):
    print list1
#11
tup1 = (1,2,3,4,5)
for tup1 in range(1,3):
    print tup1
#12
def square(x):
    y = x * x
    return y
print str(square(3))
#13
SquareRt = 25
result = square(SquareRt)
print "The result of " + str(SquareRt) + " squared is " + str(result)



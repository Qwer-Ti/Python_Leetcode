l1 = []
l2 = []
verify1 = True
verify2 = True
try:
    while verify1 == True:
        print("Enter number to l1, type stop to quit")
        a=input()
        a = int(a)
        l1.append(a)
except Exception:
    verify1 = False

try:
    while verify2 == True:
        print("Enter number to l2, type stop to quit")
        a=input()
        a = int(a)
        l2.append(a)
except Exception:
    verify2 = False

print(l1,l2)

x_first = 0
for i in range (len(l1)):
    first = l1[(-i-1)]*pow(10, (len(l1)-i))
    x_first = x_first + first

x_first = x_first/10


y_first = 0
for i in range (len(l2)):
    first = l2[(-i-1)]*pow(10, (len(l2)-i))
    y_first = y_first + first

y_first = y_first/10

summ = x_first + y_first
summ = round(summ)
print(summ)

    

    


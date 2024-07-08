def LongestSubString():
    my_str = input('input the string')
    used=[]
    a = 0
    for i in range (len(my_str)):
        if my_str[i] not in used:
            used.append(my_str[i])
            a+=1
        else:
            break

    print(used)
    print(a)

LongestSubString()


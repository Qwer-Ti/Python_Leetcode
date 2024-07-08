def ListToStr(used, delimeter = ""):
    result_str = delimeter.join(used)
    return result_str

def LongestSubString():
    my_str = input('input the string \n')
    used=[]
    final={}
    a_max=0
    max_key = 0
    for i in range (len(my_str)):
        if (my_str[i] not in used) and (a_max>=len(used)):
            used.append(my_str[i])
            a_max = a_max + 1
        else:
            final[(i-len(used))] = len(used)
            used = [my_str[i]]
            a_max=1

    #print(len(used))
    #print(used)
    #print(a_max)
    #print(final)

    try:
        max_key = max(final, key=final.get)
        max_value=final[max_key]
        #print(max_key)
        print(f"Longest substring has exactly ",max_value, "characters and is", my_str[max_key:(max_value+max_key)])
    except Exception:
        new_used = ListToStr(used,"")
        print(new_used)

LongestSubString()


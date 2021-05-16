def reverseString(stri):
    newStr=[]
    for i in range(1,len(stri)+1):
        newStr.append(stri[-i])
    newStr= ''.join(newStr)

    return newStr




print(reverseString('yoyo master'))
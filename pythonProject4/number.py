def big(num1,num2,num3):
    if num1>num2 and num1>num3:
        return 'largest is num1'
    elif  num2>num3:
        return 'n2 is high'
    else:
        return 'num3 is high'
result=big(10,2,3)
print(result)
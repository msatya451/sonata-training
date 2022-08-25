def Myfile():
    try:
        c = open('satya.txt', 'm')
        print(c.read())
    except(FileNotfoundError):
        return('not exists')
emp=Myfile()
print(emp)

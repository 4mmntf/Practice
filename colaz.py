a = input()
a = int(a)
while a>2:
    if (a%2 == 0):
        a=a/2
        print(int(a))
    if (a%2 == 1):
        a=a*3+1
        print(int(a))
print("1")
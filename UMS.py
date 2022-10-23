#無意味な数列を出すプログラムです
#受け取った桁数分出します
import random
num = input()
intor = num.isnumeric()
if intor:
    num = int(num)
    rank = 0
    while num > 0:
        randomnum = random.randint(1,10)
        rank = str(rank) + str(randomnum)
        num = num - 1
    print(rank)
else:
    print("Enter number")
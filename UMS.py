#無意味な数列を出すプログラムです
#受け取った桁数分出します
import random
num = input()
num = int(num)
rank = 0
while num > 0:
    nnum = random.randint(1, 10)
    rank = str(rank) + str(nnum) 
    num = num-1
print(rank)
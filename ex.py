import random
import numpy as np

column =int(input())#列を取得
line =int(input())#行を取得

#リストの要素を計算し現在の行と列を宣言
def ran():
    print('いまの行列は' + str(column) + '列'+ str(line) + '行です')
    return column*line
#リストを生成しcolumn列、line行に分解
list = np.arange(ran())
print(list.reshape(column,line))
i = int(column*line)
while i > 0:
    if i == 0:
        pass
    else:
        list[i-1] = random.randint(0,1)
        i = i-1

print(list.reshape(column,line))

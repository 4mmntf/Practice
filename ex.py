import random
import numpy as np
try:
    line =int(input())#行を取得
    column =int(input())#列を取得
except:
    print('数字を入力してください')
#リストの要素を計算し現在の行と列を宣言
def ran():
    print('いまの行列は' + str(line) + '行'+ str(column) + '列です')
    return line*column
#リストを生成しline行,column列に分解
list = np.arange(ran())
i = int(line*column)
#量子化
while i > 0:
    if i == 0:
        pass
    else:
        list[i-1] = random.randint(0,1)
        i = i-1
print(list.reshape(line,column))
i = int(line*column)
while i > 0:
    if list[line*column - i] == 0:
        print('□ ',end = ' ')
    else:
        print('■ ',end = ' ')
    i = i-1

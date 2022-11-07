import random
import numpy as np

column =int(input())#列を取得
line =int(input())#行を取得

#リストの要素を計算し現在の行と列を宣言
def ran(column,line):
    queue = column*line
    print('いまの行列は' + column + '列'+ line + '行です')
    return queue
#リストを生成しcolumn列、line行に分解
list=[0]*ran()
list.reshape(column,line)

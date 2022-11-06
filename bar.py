import time
import numpy as np
from fabric.colors import red ,blue ,green ,cyan

pro_size = 10
print("installing ")
for i in range(1, pro_size + 1):
    pro_bar = ('=' * i) + (' ' * (pro_size - i))
    print('\r[{0}] {1}%'.format(pro_bar, i / pro_size * 100.), end='')
    time.sleep(0.5)

print("\ncompleted")


#0~5までの配列を自動生成
a = np.arange(100)

#一次元配列aを二次元配列に変換
print(a.reshape(10, 10))

len(a)

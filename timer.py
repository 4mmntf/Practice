import PySimpleGUI as sg
import datetime
import time
timer = input()
timer = float(timer)

#時間の取得(ミリ秒)
time_now = datetime.datetime.now()
print(time_now)
#timer開始
time.sleep(timer)

print("時間だよ！！！！！！！！！！！！！！！！！！")
#デザインテーマの選択
sg.theme("white")

col1 = [sg.Text(time_now , size = (10,1) , pad = ((0,0),(10)))]

col2 = []
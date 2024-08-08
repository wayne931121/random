import time

print("請按下Enter按鍵進行抽號，號碼為0到999，按下Ctrl+C離開") #Please press Enter to get number. The numbers are 0 to 999. Press Ctrl+C to exit.
try:
    while 1:
        input()
        print(round(time.time()*1000)%1000)
except:
    pass

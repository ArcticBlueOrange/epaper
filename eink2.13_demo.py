import time
from src import *
from PIL import Image #Pillow

# Demo Configuration
X_PIXEL = 128
Y_PIXEL = 250

f = Image.open('demo.png')
f = f.convert('RGB') # conversion to RGB
data = f.load()
e = Epaper(X_PIXEL,Y_PIXEL)

rBuf = [0] * 4000
bBuf = [0] * 4000

e = Epaper(X_PIXEL,Y_PIXEL)

for y in range(250):
    for x in range(128):
       # Red CH
       if data[x,y] == (237,28,36):
           # This algorithm has bugs if ported according to C, the solution is referred to:https://www.taterli.com/7450/
           index = int(16 * y + (15 - (x - 7) / 8))
           tmp = rBuf[index]
           rBuf[index] = tmp | (1 << (x % 8))
       # Black CH
       elif data[x,y] == (255,255,255):
            index = int(16 * y + (15 - (x - 7) / 8))
            tmp = bBuf[index]
            bBuf[index] = tmp | (1 << (x % 8))

if __name__ == '__main__':
    while True:
        print("Select the action you want to take:")
        print("0\tExit")
        print("1\tUpdate")
        print("2\tFlash Black")
        print("3\tFlash White")
        print("4\tFlash Red")
        print("5\tLoad Image (red)")
        print("6\tLoad Image (black)")
        ans = input(">>")
        if ans == '0':
            break
        elif ans == '1':
            e.update()
        elif ans == '2':
            print("Flash Black")
            e.flash_red(on=False)
            e.flash_black(on=True)
        elif ans == '3':
            print("Flash White")
            e = Epaper(X_PIXEL,Y_PIXEL)
            e.flash_black(on=False)
            e.flash_red(on=False)
        elif ans == '4':
            print("Flash Red")
            e = Epaper(X_PIXEL,Y_PIXEL)
            e.flash_black(on=False)
            e.flash_red(on=True)
        elif ans == '5':
            print("Flash Image (red)")
            e.flash_red(buf=rBuf)
        elif ans == '6':
            print("Flash Image (black)")
            e.flash_black(buf=bBuf)


print("end")








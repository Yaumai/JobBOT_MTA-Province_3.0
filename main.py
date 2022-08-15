import time
import numpy as np
import pyautogui as pg
from mss import mss
import os


#область для метки и игрока
monitor1 = {
    "left": 140,
    "top": 130,
    "width": 330,
    "height": 330,
}

#админчекер
monitor2 = {
    "left": 24,
    "top": 467,
    "width": 480,
    "height": 157,
}


# метка
def find_color(our_color1,monitor1={}):
    m = mss()

    img = m.grab(monitor1)

    img_arr = np.array(img)
    # Поиск цвета
    our_map = (our_color1[2], our_color1[1], our_color1[0], 255)
    indexes = np.where(np.all(img_arr == our_map, axis=-1))
    our_crd = np.transpose(indexes)
    return our_crd


# игрок
def find_color(our_color2,monitor1={}):
    m = mss()

    img = m.grab(monitor1)

    img_arr = np.array(img)
    # Поиск цвета
    our_map = (our_color2[2], our_color2[1], our_color2[0], 255)
    indexes = np.where(np.all(img_arr == our_map, axis=-1))
    our_crd = np.transpose(indexes)
    return our_crd

#aдмин
def find_color(our_color3, monitor2={}):
    m = mss()

    img = m.grab(monitor2)

    img_arr = np.array(img)
    # Поиск цвета
    our_map = (our_color3[2], our_color3[1], our_color3[0], 255)
    indexes = np.where(np.all(img_arr == our_map, axis=-1))
    our_crd = np.transpose(indexes)
    return our_crd

#aдмин2
def find_color(our_color4, monitor2={}):
    m = mss()

    img = m.grab(monitor2)

    img_arr = np.array(img)
    # Поиск цвета
    our_map = (our_color4[2], our_color4[1], our_color4[0], 255)
    indexes = np.where(np.all(img_arr == our_map, axis=-1))
    our_crd = np.transpose(indexes)
    return our_crd


our_color1 = [0, 255, 0]  # цвет метки
our_color2 = [255, 255, 255]  # цвет игрока
our_color3 = [255, 165, 104] #админ ~->Иногда эта хуйня находит цвет другого оттенка , поэтому вписал ещё один
our_color4 = [255, 164, 104] #админ2

while True:
    time1 = time.time()
    result1 = find_color(our_color1, monitor1)
    time2 = time.time()
    time3 = time.time()
    result2 = find_color(our_color2, monitor1)
    time4 = time.time()
    result3 = find_color(our_color3, monitor2)
    result4 = find_color(our_color4, monitor2)
    if result3.__len__():
        print(time.asctime())
        x3 = result3[0][1] + monitor2.get('left')
        y3 = result3[0][0] + monitor2.get('top')
        print('АДМИН ПАЛИТ',[x3, y3])
        pid = os.getpid()
        print('id процесса ', pid)
        os.system("TASKKILL /F /IM gta_sa.exe")
        os.system("TASKKILL /F /IM CEFLauncher.exe")
    elif result4.__len__():
        print(time.asctime())
        x3 = result4[0][1] + monitor2.get('left')
        y3 = result4[0][0] + monitor2.get('top')
        print('АДМИН ПАЛИТ',[x3, y3])
        pid = os.getpid()
        print('id процесса ', pid)
        os.system("TASKKILL /F /IM gta_sa.exe")
        os.system("TASKKILL /F /IM CEFLauncher.exe")


    elif result1.__len__() and result2.__len__():
        x1 = result1[0][1] + monitor1.get('left')
        y1 = result1[0][0] + monitor1.get('top')
        x2 = result2[0][1] + monitor1.get('left')
        y2 = result2[0][0] + monitor1.get('top')
        print('Метка', time2 - time1, [x1, y1])
        print('Игрок', time4 - time3, [x2, y2])
        print()

        #бегит прямо(след турник)
        if (x2==x1 and y2>y1) or (x2 == x1+1 and y2>y1) or (x2 == x1+2 and y2>y1) or (x2==x1-1 and y2>y1) or (x2==x1-2 and y2>y1):
            time5 = time.time()
            print(time.asctime())
            pg.keyUp('s')
            pg.keyUp('d')
            pg.keyUp('a')
            pg.keyDown('w')
            time6 = time.time()
            print('Время на нажатие W: ', time6 - time5)
            print()

        #бегит направо
        elif (y2==y1 and x2<x1) or (y2==y1+1 and x2<x1)  or (y2==y1+2 and x2<x1) or (y2==y1-1 and x2<x1) or (y2==y1-2 and x2<x1):
            time5 = time.time()
            print(time.asctime())
            pg.keyUp('s')
            pg.keyUp('w')
            pg.keyUp('a')
            pg.keyDown('d')
            time6 = time.time()
            print('Время на нажатие D: ', time6 - time5)
            print()

        #бегит назад
        elif (x2==x1 and y2<y1) or (x2==x1+1 and y2<y1) or (x2==x1+2 and y2<y1) or (x2==x1-1 and y2<y1) or (x2==x1-2 and y2<y1):
            time5 = time.time()
            print(time.asctime())
            pg.keyUp('d')
            pg.keyUp('w')
            pg.keyUp('a')
            pg.keyDown('s')
            time6 = time.time()
            print('Время на нажатие S: ', time6 - time5)
            print()
        #бегит налево
        elif (y2==y1 and x2>x1) or (y2==y1+1 and x2>x1) or (y2==y1+2 and x2>x1) or (y2==y1-1 and x2>x1) or (y2==y1-2 and x2>x1):
            time5 = time.time()
            print(time.asctime())
            pg.keyUp('d')
            pg.keyUp('s')
            pg.keyUp('w')
            pg.keyDown('a')
            time6 = time.time()
            print('Время на нажатие A: ', time6 - time5)
            print()

        #бегит диагональ налево вверх
        elif (y2>y1-2 and x2>x1-2):
            time5 = time.time()
            print(time.asctime())
            pg.keyUp('d')
            pg.keyUp('s')
            pg.keyDown('w')
            pg.keyDown('a')
            time6 = time.time()
            print('Время на нажатие W+A: ', time6 - time5)
            print()

        # бегит диагональ право вверх
        elif (y2>y1-2 and x2<x1+2):
            time5 = time.time()
            print(time.asctime())
            pg.keyUp('a')
            pg.keyUp('s')
            pg.keyDown('w')
            pg.keyDown('d')
            time6 = time.time()
            print('Время на нажатие W+D: ', time6 - time5)
            print()

        # бегит диагональ право вниз
        elif (y2<y1+2 and x2<x1+2):
            time5 = time.time()
            print(time.asctime())
            pg.keyUp('a')
            pg.keyUp('w')
            pg.keyDown('s')
            pg.keyDown('d')
            time6 = time.time()
            print('Время на нажатие S+D: ', time6 - time5)
            print()

        # бегит диагональ лево низ
        elif (y2<y1+2 and x2>x1-2):
            time5 = time.time()
            print(time.asctime())
            pg.keyUp('d')
            pg.keyUp('w')
            pg.keyDown('s')
            pg.keyDown('a')
            time6 = time.time()
            print('Время на нажатие S+A: ', time6 - time5)
            print()
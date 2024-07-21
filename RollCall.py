# coding=utf-8

import pygame as pg
import random
import os
import pyttsx3
from time import sleep
import threading
import base64

def mode1windows(screen):  # 主窗口基本布局
    screen.fill((240, 240, 240))

def mode2windows(screen):  # 设置窗口基本布局
    screen.fill((240, 240, 240))

def mode3windows(screen):  # 登录窗口基本布局
    screen.fill((240, 240, 240))

def langdu(text):  # 朗读函数
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def textshow(text, rgb=(0, 0, 0), siz=72, ttf='华文楷体'):  # 渲染文字
    font = pg.font.SysFont(ttf, siz)
    text = font.render(text, True, rgb)
    return text
def encodeing(text):
    btext = text.encode('utf-8')
    coding = base64.b64encode(btext)
    return coding
def decoding(coding):
    btext = base64.b64decode(coding)
    text = btext.decode('utf-8')
    return text
def readnamelist(file):
    with open(file, 'r') as f:
        namelist = f.read()
    namelist = decoding(namelist)
    return eval(namelist)

mode = 'main'
showtext_mainwindows = '随机点名'
rolltime = 20
ifread = False
color = (0, 0, 0)
ifclick = True
ifchoice = False
times = 0
rollspeed = 20  # 每秒
thread = None
namelist = readnamelist('namelist.bin')

pg.init()  # 初始化
windows = pg.display.set_mode((385, 141))
pg.display.set_caption('RollCall')
mode1windows(windows)
windows.blit(textshow('随机点名', color), (46, 19))

while True:
    events = pg.event.get()  # 获取事件

    for event in events:  # 判断退出
        if event.type == pg.QUIT:
            pg.quit()
            os._exit(0)

    if mode == 'main':  # 进入主窗口
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if event.pos[0] >= 354 and event.pos[1] <= 31:
                mode = 'login'
                ifclick = True
                times = 1
                ifchoice = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and ifclick == True:
                ifchoice = True

    elif mode == 'login':  # 进入登录窗口
        mode3windows(windows)

    elif mode == 'setting':  # 进入设置窗口
        mode2windows(windows)

    if ifchoice == True:
        times += 1
        mode1windows(windows)
        showtext_mainwindows = random.choice(namelist)
        windows.blit(textshow(showtext_mainwindows, color), (46 + (4 - len(showtext_mainwindows)) * 73.25 / 2, 25))
        if times == rolltime:
            ifread = True
            times = 1
            ifchoice = False
        sleep(1 / rollspeed)

    pg.display.update()

    if ifread == True:
        thread = threading.Thread(target=langdu, args=(showtext_mainwindows,))
        thread.start()
        ifread = False
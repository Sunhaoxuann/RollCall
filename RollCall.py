# coding=utf-8

import pygame as pg
import random
import os
import pyttsx3
from time import sleep
import threading

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

mode = 'main'
showtext_mainwindows = '随机点名'
namelist = ['叶杨阳', '肖逸凡', '王沐恩', '黄皓轩', '项涵哲', '邹帆', '闻张依', '翁睿毅', '李御轩', '张峰铭', '韦思桐', '沈凯昕', '林浩', '吴珈栩', '袁晓晴', '于妙盈', '俞昭阳', '申屠绍越', '姚智宇', '陶奕畅',
            '孙昊轩', '高智杰', '严天浩', '李嘉怡', '何相南', '黄圣曦', '周炜昊', '吴文萱', '李乐山', '殷一铭', '蒋一凡', '孙周哲翊', '沈雨涵', '程天宇', '郑杰', '蒋哲聪', '徐书亚', '林馨雯', '方浩如', '刘翔',
            '边峻熙', '叶俊浩', '张可维', '李宏振', '高浩哲', '产洲俊', '王博辉', '陈沈捷']
rolltime = 20
ifread = False
color = (0, 0, 0)
ifclick = True
ifchoice = False
times = 0
rollspeed = 20  # 每秒
thread = None

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
# coding=utf-8

import json
import pygame as pg
import random
import os
import pyttsx3
from time import sleep
import threading
import base64
import pandas as pd
import sys


def program_init():
    def init_filelines():

        writelines = [b'Wyflj7bmnajpmLMnLCAn6IKW6YC45YehJywgJ+eOi+aykOaBqScsICfpu4TnmpPovaknLCAn6aG55ra15ZOyJywgJ+mCueW'
                      b'4hicsICfpl7vlvKDkvp0nLCAn57+B552/5q+FJywgJ+adjuW+oei9qScsICflvKDls7Dpk60nLCAn6Z+m5oCd5qGQJywgJ+'
                      b'ayiOWHr+aYlScsICfmnpfmtaknLCAn5ZC054+I5qCpJywgJ+iigeaZk+aZtCcsICfkuo7lppnnm4gnLCAn5L+e5pit6ZizJ'
                      b'ywgJ+eUs+WxoOe7jei2iicsICflp5rmmbrlrocnLCAn6Zm25aWV55WFJywgJ+WtmeaYiui9qScsICfpq5jmmbrmnbAnLCAn'
                      b'5Lil5aSp5rWpJywgJ+adjuWYieaAoScsICfkvZXnm7jljZcnLCAn6buE5Zyj5pumJywgJ+WRqOeCnOaYiicsICflkLTmlof'
                      b'okLEnLCAn5p2O5LmQ5bGxJywgJ+aut+S4gOmTrScsICfokovkuIDlh6EnLCAn5a2Z5ZGo5ZOy57+KJywgJ+ayiOmbqOa2tS'
                      b'csICfnqIvlpKnlrocnLCAn6YOR5p2wJywgJ+iSi+WTsuiBqicsICflvpDkuabkuponLCAn5p6X6aao6ZuvJywgJ+aWuea1q'
                      b'eWmgicsICfliJjnv5QnLCAn6L655bO754aZJywgJ+WPtuS/iua1qScsICflvKDlj6/nu7QnLCAn5p2O5a6P5oyvJywgJ+mr'
                      b'mOa1qeWTsicsICfkuqfmtLLkv4onLCAn546L5Y2a6L6JJywgJ+mZiOayiOaNtydd\r\n', b'MDEyMzQ1']

        with open('.\\.RollCall\\config.bin', 'wb') as f:
            for i in writelines:
                f.write(i)

    pg.init()  # 初始化pygame

    # 初始化文件
    if not os.path.isdir('.\\.RollCall'):
        os.mkdir('.\\.RollCall')
        init_filelines()
    elif os.path.isdir('.\\.RollCall') and not os.path.isfile('.\\.RollCall\\config.bin'):
        init_filelines()


def mode1windows(screen):  # 主窗口基本布局
    screen.fill((240, 240, 240))
    screen.blit(textshow('·', black, 20), (348, -1))
    screen.blit(textshow('·', black, 20), (358, -1))
    screen.blit(textshow('·', black, 20), (368, -1))


def mode2windows(screen):  # 设置窗口基本布局
    screen.fill((240, 240, 240))
    screen.blit(textshow('←返回', (113, 96, 232), 15), (30, 100))


def mode3windows(screen):  # 登录窗口基本布局
    screen.fill((240, 240, 240))
    screen.blit(textshow('请输入密码', black, 20), (25, 15))
    screen.blit(textshow('_ _ _ _ _ _', black, 20), (33, 60))
    screen.blit(textshow('1', black, 30), (210, 14))
    screen.blit(textshow('4', black, 30), (210, 54))
    screen.blit(textshow('7', black, 30), (210, 94))
    screen.blit(textshow('2', black, 30), (250, 14))
    screen.blit(textshow('5', black, 30), (250, 54))
    screen.blit(textshow('8', black, 30), (250, 94))
    screen.blit(textshow('3', black, 30), (290, 14))
    screen.blit(textshow('6', black, 30), (290, 54))
    screen.blit(textshow('9', black, 30), (290, 94))
    screen.blit(textshow('0', black, 30), (330, 54))
    screen.blit(textshow('确定', (113, 96, 232), 20), (320, 100))
    screen.blit(textshow('删除', (113, 96, 232), 20), (320, 20))
    screen.blit(textshow('←返回', (113, 96, 232), 15), (30, 100))

    # screen.blit(textshow('1 2 3 4 5 6', black, 21), (33, 60))
    # pg.draw.rect(screen, (225, 225, 225), (25, 50, 335, 25), 0)
    # pg.draw.rect(screen, (220, 220, 220), (290, 90, 70, 25), 0)


def messagewindows(screen, text, rgb=(0, 0, 0), siz=72, ttf='华文楷体'):  # 信息窗口
    screen.fill((240, 240, 240))
    screen.blit(textshow(text, rgb, siz, ttf), (25, 50))


def langdu(text):  # 朗读函数
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def textshow(text, rgb=(0, 0, 0), siz=72, ttf='华文楷体'):  # 渲染文字
    font = pg.font.SysFont(ttf, siz)
    text = font.render(text, True, rgb)
    return text


def encodeing(text):  # 编码加密函数
    btext = text.encode('utf-8')
    coding = base64.b64encode(btext)
    return coding


def decoding(coding):  # 编码解码函数
    btext = base64.b64decode(coding)
    text = btext.decode('utf-8')
    return text


def readbinfile(file):  # 读取文件函数
    with open(file, 'r') as f:
        namelist = f.readline()
        password = f.readline()
    namelist = decoding(namelist)
    password = decoding(password)
    return eval(namelist), password


def writebinfile(file, namelist, password):  # 写入文件函数
    namelist = encodeing(str(namelist))
    password = encodeing(str(password))
    with open(file, 'wb') as f:
        f.write(namelist)
        f.write(password)


def _var(vars):
    print(f"value:{vars}, type:{type(vars)}, len:{len(vars)}")


class nothing(object):
    def type(self):
        return None


program_init()  # 初始化
windows = pg.display.set_mode((385, 141))
pg.display.set_caption('RollCall')

# 设定基本参数
# main
ifclick = True
main_ifchoice = False
times = 0
rollspeed = 20  # 每秒
main_showtext_mainwindows = '随机点名'
rolltime = 20
main_read = False
main_repeat = True
main_repeat_ifclick = True
main_repeat_times = 0

# login
showpassword = ''
login_password_statu = 1
mode = 'main'

# glob
black = (0, 0, 0)
thread = None
namelist, password = readbinfile('.\\.RollCall\\config.bin')
red = (255, 0, 0)
green = (0, 150, 0)

while True:

    # debug!!!-----------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    # mode = 'main'

    if mode == 'main':
        while True:

            # 获取事件
            events = pg.event.get()

            # 退出判断
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()

            # 点击判断
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 320 and event.pos[
                1] > 120 and main_repeat_ifclick and main_ifchoice == False:
                main_repeat = not main_repeat
                main_repeat_ifclick = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] >= 351 and event.pos[1] <= 25:
                mode = 'login'
                main_ifchoice = False
                ifclick = True
                times = 0
                break
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and ifclick and main_repeat_ifclick:
                main_ifchoice = True
                main_ifclick = False

            # 显示文字处理
            if main_ifchoice:
                times += 1
                if times == rolltime:
                    main_ifchoice = False
                    ifclick = True
                    main_read = True
                    times = 0
                main_showtext_mainwindows = random.choice(namelist)
                sleep(1 / rollspeed)

            # 延时
            if not main_repeat_ifclick:
                main_repeat_times += 1
                if main_repeat_times == 10:
                    main_repeat_ifclick = True
                    main_repeat_times = 0

            # 渲染
            mode1windows(windows)
            windows.blit(textshow(main_showtext_mainwindows, black),
                         (46 + (4 - len(main_showtext_mainwindows)) * 73.25 / 2, 25))
            if not main_ifchoice:
                pg.draw.rect(windows, (0, 0, 0), (315, 120, 70, 21), 2)
                windows.blit(textshow('重复:', black, 15), (315, 120))
                if main_repeat:
                    windows.blit(textshow('True', (0, 150, 0), 15), (350, 120))
                else:
                    windows.blit(textshow('False', (150, 0, 0), 15), (350, 120))
            pg.display.update()

            # 声音渲染
            if main_read:
                if thread is not None:
                    thread.join()

                thread = threading.Thread(target=langdu, args=(main_showtext_mainwindows,))
                thread.start()
                main_read = False

    elif mode == 'login':
        tempstr = ""
        while True:
            # 运算

            # 获取事件
            events = pg.event.get()

            # 退出判断
            for event in events:
                if event.type == pg.QUIT:
                    os._exit(0)

            # 点击判断

            if not ifclick:
                if times >= 2:  # 防止点击过快
                    ifclick = True
                    times = 0
                times += 1

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                if event.pos[0] in range(29, 76) and event.pos[1] in range(99, 121):
                    mode = 'main'
                    event = nothing()
                    break

                if ifclick:
                    login_password_statu = 1
                    if event.pos[0] in range(196, 236) and event.pos[1] in range(14, 54):
                        tempstr += "1"
                        ifclick = False
                    if event.pos[0] in range(236, 276) and event.pos[1] in range(14, 54):
                        tempstr += "2"
                        ifclick = False
                    if event.pos[0] in range(276, 316) and event.pos[1] in range(14, 54):
                        tempstr += "3"
                        ifclick = False
                    if event.pos[0] in range(196, 236) and event.pos[1] in range(54, 94):
                        tempstr += "4"
                        ifclick = False
                    if event.pos[0] in range(236, 276) and event.pos[1] in range(54, 94):
                        tempstr += "5"
                        ifclick = False
                    if event.pos[0] in range(276, 316) and event.pos[1] in range(54, 94):
                        tempstr += "6"
                        ifclick = False
                    if event.pos[0] in range(196, 236) and event.pos[1] in range(94, 134):
                        tempstr += "7"
                        ifclick = False
                    if event.pos[0] in range(236, 276) and event.pos[1] in range(94, 134):
                        tempstr += "8"
                        ifclick = False
                    if event.pos[0] in range(276, 316) and event.pos[1] in range(94, 134):
                        tempstr += "9"
                        ifclick = False
                    if event.pos[0] in range(316, 356) and event.pos[1] in range(54, 94):
                        tempstr += "0"
                        ifclick = False
                    if event.pos[0] in range(316, 371) and event.pos[1] in range(14, 54):
                        tempstr = tempstr[:-1]
                        ifclick = False  # 删除按键

                    if len(tempstr) >= 6:
                        tempstr = tempstr[:6]

                    if len(tempstr) == 6 or (event.pos[0] in range(316, 371) and event.pos[1] in range(94, 134)):
                        if tempstr == password:
                            mode = 'setting'
                            login_password_statu = 3
                        else:
                            login_password_statu = 2
                            tempstr = ""
                            event = nothing()

            showpassword = ""
            for i in tempstr:
                showpassword += i
                showpassword += " "

            # 渲染
            if login_password_statu == 1:
                mode3windows(windows)
            elif login_password_statu == 2:
                mode3windows(windows)
                pg.draw.rect(windows, red, (0, 0, 385, 20), 0)
                windows.blit(textshow('密码错误', (255, 255, 255), 15), (25, 0))
            elif login_password_statu == 3:
                mode3windows(windows)
                pg.draw.rect(windows, green, (0, 0, 385, 20), 0)
                windows.blit(textshow('密码正确', (255, 255, 255), 15), (25, 0))
                windows.blit(textshow(showpassword, black, 21), (33, 60))
                pg.display.update()
                sleep(1)
                break

            windows.blit(textshow(showpassword, black, 21), (33, 60))

            pg.display.update()

    elif mode == 'setting':
        while True:
            # 运算
            events = pg.event.get()  # 获取事件
            for event in events:
                if event.type == pg.QUIT:
                    os._exit(0)

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                if event.pos[0] in range(29, 76) and event.pos[1] in range(99, 121):
                    mode = 'main'
                    event = nothing()
                    break

            # 渲染
            mode2windows(windows)

            windows.blit(textshow('导入名单', (0, 0, 0), 15), (5, 5))
            pg.draw.rect(windows, (0, 0, 0), (5, 5, 60, 20), 1)

            windows.blit(textshow('生成名单导入模板', (0, 0, 0), 15), (40, 30))
            pg.draw.rect(windows, (0, 0, 0), (40, 30, 121, 20), 1)

            windows.blit(textshow('┕', (0, 0, 0), 15), (10, 30))

            pg.display.update()

# HISTORY CODE
# '''
# while True:
#     events = pg.event.get()  # 获取事件
#
#     for event in events + [nothing]:  # 判断退出
#         if event.type == pg.QUIT:
#             pg.quit()
#             os._exit(0)
#
#         else:
#
#             if mode == 'main':  # 进入主窗口
#                 if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
#                     if event.pos[0] >= 351 and event.pos[1] <= 25:
#                         mode = 'login'
#                     elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and ifclick == True:
#                         ifchoice = True
#
#             elif mode == 'login':  # 进入登录窗口
#                 if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # 鼠标点击检测
#                     if event.pos[0] in range(25, 72) and event.pos[1] in range(90, 112): # 返回按钮
#                         homewindows(windows)
#                         mode = 'main'
#                         event = nothing()
#                         continue
#
#                     if event.pos[0] in range(25, 360) and event.pos[1] in range(50, 75): # 输入框激活判断
#                         active = True
#                     else:
#                         active = False
#
#                 if active:
#                     ...
#                     # if event.type == pg.KEYDOWN:  # 键盘按下
#                     #     if events.key == pg.K_BACKSPACE:  # 删除
#                     #         logging.info("delete")
#                     #     elif events.key == pg.K_RETURN:  # 确认
#                     #         logging.info("enter")
#                     #     elif events.key == pg.K_0:
#                     #         logging.info("0")
#
#                 mode3windows(windows)
#
#             elif mode == 'setting':  # 进入设置窗口
#                 mode2windows(windows)
#
#             if ifchoice == True:
#                 times += 1
#                 mode1windows(windows)
#                 showtext_mainwindows = random.choice(namelist)
#                 windows.blit(textshow(showtext_mainwindows, black), (46 + (4 - len(showtext_mainwindows)) * 73.25 / 2, 25))
#
#                 if times == rolltime:
#                     ifread = True
#                     times = 1
#                     ifchoice = False
#                 sleep(1 / rollspeed)
#
#             pg.display.update()
#
#             if ifread == True:
#                 if thread is not None:
#                     thread.join()
#
#                 thread = threading.Thread(target=langdu, args=(showtext_mainwindows,))
#                 thread.start()
#                 ifread = False
# '''
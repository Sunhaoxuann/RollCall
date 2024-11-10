import random
import tkinter as tk
from tkinter import font

students = ["林馨雯","方浩如","吴珈栩","林浩","沈凯昕","韦思桐","张峰铭","翁睿毅","李御轩","陈沈捷",
"李宏振","产洲俊","高浩哲","王博辉","刘翔","张可维","边峻熙","叶俊浩","徐书亚","郑杰",
"蒋哲聪","沈雨涵","孙周哲翊","程天宇","李乐山","蒋一凡","殷一铭","陶奕畅","李嘉怡","黄圣曦",
"周炜昊","何相南","孙昊轩","严天浩","姚智宇","吴文萱","高智杰","于妙盈","俞昭阳","申屠绍越",
"袁晓晴","王沐恩","闻张依","黄皓轩","项涵哲","肖逸凡","邹帆","叶杨阳"]

def call_student():
    chosen_student = random.choice(students)
    result_label.config(text=f"天选之子，你被点名了：{chosen_student}")

root = tk.Tk()
root.title("随机点名")

# 设置较大的窗口尺寸
root.geometry("500x300")

# 设置背景颜色
root.configure(bg="#f0f0f0")

# 创建自定义字体
custom_font = font.Font(family="Helvetica", size=16, weight="bold")

button = tk.Button(root, text="点名", command=call_student, bg="#4CAF50", fg="white", font=custom_font)
button.pack(pady=40)

result_label = tk.Label(root, text="", font=custom_font, bg="#f0f0f0")
import random
import tkinter as tk
from tkinter import font

# 定义学生名单列表
students = ["林馨雯","方浩如","吴珈栩","林浩","沈凯昕","韦思桐","张峰铭","翁睿毅","李御轩","陈沈捷",
"李宏振","产洲俊","高浩哲","王博辉","刘翔","张可维","边峻熙","叶俊浩","徐书亚","郑杰",
"蒋哲聪","沈雨涵","孙周哲翊","程天宇","李乐山","蒋一凡","殷一铭","陶奕畅","李嘉怡","黄圣曦",
"周炜昊","何相南","孙昊轩","严天浩","姚智宇","吴文萱","高智杰","于妙盈","俞昭阳","申屠绍越",
"袁晓晴","王沐恩","闻张依","黄皓轩","项涵哲","肖逸凡","邹帆","叶杨阳"]

def update_display():
    """
    不断随机更新显示的学生名字。
    如果 updating 为 True，则从学生名单中随机选择一个学生名字显示在标签上，
    并设置每隔 100 毫秒再次调用自身以实现不断更新。
    """
    global current_student
    if updating:
        current_student = random.choice(students)
        result_label.config(text=current_student)
        root.after(100, update_display)

def call_student():
    """
    当点击点名按钮时被调用。
    将 updating 设置为 False，禁用按钮，
    并在 2000 毫秒后调用一系列操作以恢复按钮状态并重新开始更新显示。
    """
    global updating
    updating = False
    button.config(state=tk.DISABLED)
    root.after(2000, lambda: (button.config(state=tk.NORMAL), set_updating(True), update_display()))

def set_updating(value):
    """
    设置 updating 变量的值。
    :param value: 要设置给 updating 的值，True 或 False。
    """
    global updating
    updating = value

# 创建 Tkinter 主窗口
root = tk.Tk()
root.title("课堂随机点名系统")

# 设置窗口大小为 500x300 像素
root.geometry("500x300")
# 设置窗口背景颜色为 #f0f0f0
root.configure(bg="#f0f0f0")

# 创建自定义字体
custom_font = font.Font(family="Helvetica", size=16, weight="bold")

# 创建点名按钮，绑定 call_student 函数，设置背景颜色、文本颜色和字体
button = tk.Button(root, text="点名", command=call_student, bg="#4CAF50", fg="white", font=custom_font)
button.pack(pady=40)

# 创建用于显示被点名学生名字的标签，设置字体和背景颜色
result_label = tk.Label(root, text="", font=custom_font, bg="#f0f0f0")
result_label.pack(pady=20)

current_student = ""
updating = True
# 开始不断更新显示学生名字
update_display()

# 进入 Tkinter 主循环
root.mainloop()
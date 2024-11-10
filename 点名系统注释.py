import random
import tkinter as tk
from tkinter import font
# 导入 random 模块用于随机选择学生名字
# 导入 tkinter 模块并别名为 tk，用于创建图形用户界面
# 从 tkinter 模块中导入 font 模块，用于创建自定义字体

students = ["林馨雯","方浩如","吴珈栩","林浩","沈凯昕","韦思桐","张峰铭","翁睿毅","李御轩","陈沈捷",
"李宏振","产洲俊","高浩哲","王博辉","刘翔","张可维","边峻熙","叶俊浩","徐书亚","郑杰",
"蒋哲聪","沈雨涵","孙周哲翊","程天宇","李乐山","蒋一凡","殷一铭","陶奕畅","李嘉怡","黄圣曦",
"周炜昊","何相南","孙昊轩","严天浩","姚智宇","吴文萱","高智杰","于妙盈","俞昭阳","申屠绍越",
"袁晓晴","王沐恩","闻张依","黄皓轩","项涵哲","肖逸凡","邹帆","叶杨阳"]
# 定义一个列表，包含学生的名字

def call_student():
    """
    定义一个函数，用于随机点名。
    当这个函数被调用时，从 students 列表中随机选择一个学生名字，
    然后更新 result_label 的文本内容，显示被点名的学生信息。
    """
    chosen_student = random.choice(students)
    result_label.config(text=f"天选之子，你被点名了：{chosen_student}")

root = tk.Tk()
root.title("课堂随机点名系统")
# 创建一个 Tkinter 的主窗口对象，并设置窗口标题为"课堂随机点名系统"

# 设置较大的窗口尺寸
root.geometry("500x300")
# 设置窗口的大小为 500 像素宽，300 像素高

# 设置背景颜色
root.configure(bg="#f0f0f0")
# 将窗口的背景颜色设置为浅灰色（十六进制颜色代码 #f0f0f0）

# 创建自定义字体
custom_font = font.Font(family="Helvetica", size=16, weight="bold")
# 创建一个自定义字体对象，字体为 Helvetica，大小为 16，加粗

button = tk.Button(root, text="点名", command=call_student, bg="#4CAF50", fg="white", font=custom_font)
button.pack(pady=40)
# 创建一个按钮对象，放置在 root 主窗口中。
# 按钮的文本为"点名"，点击按钮时会调用 call_student 函数。
# 按钮的背景颜色为绿色（十六进制颜色代码 #4CAF50），文本颜色为白色。
# 按钮使用自定义字体 custom_font。
# 使用 pack 方法将按钮放置在窗口中，并设置垂直方向的填充为 40 像素。

result_label = tk.Label(root, text="", font=custom_font, bg="#f0f0f0")
result_label.pack(pady=20)
# 创建一个标签对象，放置在 root 主窗口中。
# 标签的初始文本为空字符串，使用自定义字体 custom_font，背景颜色为浅灰色。
# 使用 pack 方法将标签放置在窗口中，并设置垂直方向的填充为 20 像素。

root.mainloop()
# 启动 Tkinter 的主循环，使窗口持续显示并等待用户交互。
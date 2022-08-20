# 剪刀石头布Python练习程序v1.0 By HAO
import random
from tkinter import *


class GAME_UI:

    def __init__(self, init_window):
        self.init_window = init_window

    # 基础界面
    def start_game_ui(self):
        global user_var
        user_var = StringVar()
        user_var.set("")
        global cpu_var
        cpu_var = StringVar()
        cpu_var.set("")
        global result_var
        result_var = StringVar()
        result_var.set("")
        # 界面各种元素生成
        self.init_window.geometry("300x400")
        self.init_window.title("石头剪刀布游戏V0.1")
        self.Label = Label(self.init_window,
                           text='剪刀石头布游戏', font=('Arial', 24),
                           width=20, height=4)
        self.Label_user_intro = Label(self.init_window, relief=RAISED,
                                font=('Arial', 12), text='玩家: ')
        self.Label_user = Label(self.init_window,
                                font=('Arial', 15), textvariable=user_var)
        self.Label_cpu_intro = Label(self.init_window, text='电脑: ', relief=RAISED,
                               font=('Arial', 12))
        self.Label_cpu = Label(self.init_window, textvariable=cpu_var,
                               font=('Arial', 15))
        self.Label_result_intro = Label(self.init_window, text='结果:', relief=RAISED,
                                  font=('Arial', 12))
        self.Label_result = Label(self.init_window, textvariable=result_var,
                                  font=('Arial', 15))
        self.scissor_button = Button(self.init_window, text='剪刀', height=3, command=lambda: self.who_wins(1))
        self.rock_button = Button(self.init_window, text='石头', height=3, command=lambda: self.who_wins(2))
        self.peper_button = Button(self.init_window, text='布', height=3, command=lambda: self.who_wins(3))

        # 排列各种元素
        self.Label.grid(column=0, row=0, columnspan=5, sticky='E')
        self.Label_result_intro.grid(column=0, row=8, sticky='W', pady=10)
        self.Label_result.grid(column=1, row=8, sticky='W', pady=10)
        self.Label_user_intro.grid(column=0, row=4, sticky='W', )
        self.Label_user.grid(column=1, row=4, sticky='W')
        self.Label_cpu_intro.grid(column=0, row=5, sticky='W')
        self.Label_cpu.grid(column=1, row=5, sticky='W')
        self.scissor_button.grid(column=0, row=12, sticky='S', pady=80)
        self.rock_button.grid(column=1, row=12, sticky='S', pady=80)
        self.peper_button.grid(column=2, row=12, sticky='S', pady=80)

    # 胜负功能
    def who_wins(self, user_choice):
        dic = {1: '剪刀', 2: '石头', 3: '布'}
        cpu_number = random.randint(1, 3)
        # user_var.set("")
        # cpu_var.set("")
        # result_var.set("")
        user_var.set('您优雅的打出了' +'"'+ dic.get(user_choice)+'"')
        cpu_var.set('电脑愤怒的打出了' +'"'+ dic.get(cpu_number)+'"')
        minus_result = user_choice - cpu_number
        if minus_result == 0:
            result_var.set('最终结果-->平局收场😄')
        elif minus_result == 1 or minus_result == -2:
            result_var.set('最终结果-->您赢了✌️')
        else:
            result_var.set('最终结果-->您输了😢')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_ui = Tk()
    my_game = GAME_UI(init_ui)
    my_game.start_game_ui()
    init_ui.mainloop()

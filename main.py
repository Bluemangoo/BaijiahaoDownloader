"""
@Author: Bluemangoo
@Date: 2022.11
@Copyright: 2022 Bluemangoo. All rights reserved.
@Description: 
"""
from tkinter import END

# "https://baijiahao.baidu.com/s?id=1734601670138903003"
import downloader
import tkinter


class Application:
    def __init__(self, window_name):
        self.RightWindowLabel = None
        self.LeftText = None
        self.TransButton = None
        self.RightText = None
        self.LeftWindowLabel = None
        self.windowName = window_name

    def window_box(self):
        # 标题和标签
        self.windowName.title("百家号文章下载器")
        self.windowName.geometry('605x150+550+150')
        self.LeftWindowLabel = tkinter.Label(self.windowName, text="请输入链接", padx=100)
        self.LeftWindowLabel.grid(column=0, row=0)

        # 文本框
        self.LeftText = tkinter.Text(self.windowName, width=20, height=1)
        self.LeftText.grid(column=0, row=1, rowspan=2, columnspan=2)
        self.RightText = tkinter.Text(self.windowName, width=20, height=1)
        self.RightText.grid(column=0, row=1, rowspan=2, columnspan=2)

        # 按钮
        self.TransButton = tkinter.Button(self.windowName, text="下载", command=self.bmi_calculate, width=10)
        self.TransButton.grid(column=2, row=2)

    def bmi_calculate(self):
        self.RightText.delete(1.0, END)
        self.RightText.insert(1.0, "下载中\n")
        print(self.LeftText.get(END))
        # downloader.main(self.LeftText.get(END))
        self.RightText.insert(1.0, "下载完成")


def main():
    window = tkinter.Tk()
    app = Application(window)
    app.window_box()
    window.mainloop()


if __name__ == "__main__":
    main()

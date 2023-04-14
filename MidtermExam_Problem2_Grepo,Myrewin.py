from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.lbl5 = Label(win, text="Metric Units of Length", font=("Verdana"), fg="Black")
        self.lbl5.place(x=200, y=15)

        self.lbl1 = Label(win, text="Enter the distance in centimeters(cm): ", fg="Black")
        self.lbl1.place(x=100, y=60)
        self.lbl2 = Label(win, text="Conversion into meter(m): ", fg="Black")
        self.lbl2.place(x=100, y=90)
        self.lbl3 = Label(win, text="Conversion into kilometer(km): ", fg="Black")
        self.lbl3.place(x=100, y=120)

        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=310, y=60)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=310, y=90)
        self.txt3 = Entry(win, bd=1)
        self.txt3.place(x=310, y=120)

        self.btnConvert = Button(win, text="Convert", bg="white", command=self.convert)
        self.btnConvert.place(x=300, y=255, anchor="center")

    def Convert(self, convert):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 / 100
        result = num1 / 1000


window = Tk()
MyWin = MyWindow(window)
window.geometry("600x400")
window.title("Midterm Exam Problem 2")
window.mainloop()

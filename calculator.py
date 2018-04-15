from tkinter import *
from tkinter import ttk
import math

class calculator(Frame):
    def __init__(self, master):
        super(calculator, self).__init__(master)
        self.tugas = ""
        self.input = StringVar()
        self.grid()
        self.isi()
        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)

        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

    def isi(self):
        self.masukkin = ttk.Entry(self,
                                  textvar=self.input, width=50, justify=RIGHT)
        self.masukkin.grid(columnspan=10)

        self.masukkin.insert(0, "0")

        self.angka1 = ttk.Button(self, text="1",
                                 command=lambda: self.operator(1))
        self.angka1.grid(column=0, row=1)

        self.angka2 = ttk.Button(self, text="2",
                                 command=lambda: self.operator(2))
        self.angka2.grid(column=1, row=1)

        self.angka3 = ttk.Button(self, text="+",
                                 command=lambda: self.operator("+"))
        self.angka3.grid(column=2, row=1)

        self.angka4 = ttk.Button(self, text="=",
                                 command=self.samadengan)
        self.angka4.grid(column=4, row=1)

        self.angka4 = ttk.Button(self, text="hapus",
                                 command=self.hapus)
        self.angka4.grid(column=4, row=2)

        self.angka5 = ttk.Button(self, text="3",
                                 command=lambda: self.operator(3))
        self.angka5.grid(column=0, row=2)

        self.angka6 = ttk.Button(self, text="4",
                                 command=lambda: self.operator(4))
        self.angka6.grid(column=1, row=2)

        self.angka7 = ttk.Button(self, text="5",
                                 command=lambda: self.operator(5))
        self.angka7.grid(column=0, row=3)

        self.angka8 = ttk.Button(self, text="6",
                                 command=lambda: self.operator(6))
        self.angka8.grid(column=1, row=3)

        self.angka9 = ttk.Button(self, text="7",
                                 command=lambda: self.operator(7))
        self.angka9.grid(column=0, row=4)

        self.angka10 = ttk.Button(self, text="8",
                                  command=lambda: self.operator(8))
        self.angka10.grid(column=1, row=4)

        self.angka11 = ttk.Button(self, text="9",
                                  command=lambda: self.operator(9))
        self.angka11.grid(column=2, row=4)

        self.angka12 = ttk.Button(self, text="0",
                                  command=lambda: self.operator(0))
        self.angka12.grid(column=2, row=3)

        self.angka3 = ttk.Button(self, text="/",
                                 command=lambda: self.operator("/"))
        self.angka3.grid(column=2, row=2)

        self.angka3 = ttk.Button(self, text="- ",
                                 command=lambda: self.operator("-"))
        self.angka3.grid(column=4, row=3)


    def operator(self, number):
        self.tugas = str(self.tugas) + str(number)
        self.input.set(self.tugas)

    def samadengan(self):
        jumlahnya = str(eval(self.tugas))
        self.input.set(jumlahnya)

    def hapus(self):
        self.tugas = ""
        self.masukkin.delete(0, END)
        self.masukkin.insert(0, "0")


kalkulator = Tk()

kalkulator.title("kalkulator by Samba Alfaraby")

x = calculator(kalkulator)

kalkulator.mainloop()

from pytube import YouTube
from tkinter import *
from tkinter import ttk

def downlod(lnk):
    YouTube(lnk).streams.get_highest_resolution().download()
    link.delete(0, END)


def main():
    global link

    root = Tk()
    root.geometry("400x200")

    Label(text="Пожалуйсьа вставте ссылку с YouTube,\n чтобы скачать его в максимально возможном расширении: ", font=("Arial", 10)).pack()
    
    link = ttk.Entry(width=40)
    link.pack()

    ttk.Button(text='Скачать', command=lambda: downlod(link.get())).pack()

    root.mainloop()

main()

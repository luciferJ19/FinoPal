import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':

    userName = tk.StringVar()

    root = tk.Tk()
    root.title("FinoPal")
    root.geometry("{}x{}".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    frameName = tk.Frame(root)
    frameName.pack(side="top", anchor= "w", padx = 10, pady=50)

    frameAge = tk.Frame(root)
    frameAge.pack(side="top", anchor= "w", padx = 10, pady =10)

    nameLabel = tk.Label(frameName, text= "NAME: ", padx=10, pady = 10, bg = "grey", fg = "black")
    nameLabel.pack(side = "left")

    nameEntry = tk.Entry(frameName, textvariable= userName, width=22)
    nameEntry.pack(side="left", padx=10)

    ageLabel = tk.Label(frameAge, text= "AGE: ", padx=10, pady=10, bg = "grey", fg = "black")
    ageLabel.pack(side ="left", anchor="e")

    ageEntry = tk.Entry(frameAge, )


    root.mainloop()

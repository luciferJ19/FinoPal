import tkinter as tk
from tkinter import ttk

def backendMain(name, age, income, debt, savings, expenses):
    userNameB = name
    userAgeB = age
    userIncome = income
    userDebt = debt
    userSavings = savings
    userExpenses = expenses

    if (userAge <= 14):
        x = 0  #code to be defined
    elif (userAge > 14 and userAge < 18):
        x = 0  # code to be defined
    elif (userAge >= 18 and userAge <=28):
        x = 0  # code to be defined
    elif (userAge > 28 and userAge <= 50):
        x = 0  # code to be defined
    elif (userAge > 50 and userAge <=65):
        x = 0  # code to be defined
    elif (userAge > 65):
        x = 0  # code to be defined


if __name__ == '__main__':

    root = tk.Tk()
    root.title("FinoPal")
    root.geometry("{}x{}".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    userName = tk.StringVar()
    userAge = tk.IntVar()
    userIncome = tk.IntVar()
    userDebt = tk.IntVar()
    userSavings = tk.IntVar()
    userExpenses = tk.IntVar()

    frameName = tk.Frame(root)
    frameName.pack(side="top", anchor= "w", padx = 10, pady=50)

    frameAge = tk.Frame(root)
    frameAge.pack(side="top", anchor= "w", padx = 10, pady =10)

    frameIncome = tk.Frame(root)
    frameIncome.pack(side="top", anchor="w", padx=10, pady=10)

    frameDebt = tk.Frame(root)
    frameDebt.pack(side="top", anchor="w", padx=10, pady=10)

    frameSavings = tk.Frame(root)
    frameSavings.pack(side="top", anchor="w", padx=10, pady=10)

    frameExpenses = tk.Frame(root)
    frameExpenses.pack(side="top", anchor="w", padx =10, pady=10)

    frameButtons = tk.Frame(root)
    frameButtons.pack(side ="top", anchor="w", padx=10, pady=40)

    nameLabel = tk.Label(frameName, text= "NAME: ", padx=10, pady = 10, bg = "grey", fg = "black")
    nameLabel.pack(side = "left")
    nameEntry = tk.Entry(frameName, textvariable= userName, width=22)
    nameEntry.pack(side="left", padx=10)

    ageLabel = tk.Label(frameAge, text= "AGE: ", padx=10, pady=10, bg = "grey", fg = "black")
    ageLabel.pack(side ="left", anchor="e")
    ageEntry = tk.Entry(frameAge, textvariable=userAge, width = 3)
    ageEntry.pack(side="left", padx=10)

    incomeLabel = tk.Label(frameIncome, text = "INCOME: ", padx=10, pady=10, bg = "grey", fg = "black")
    incomeLabel.pack(side = "left", anchor ="e")
    incomeEntry = tk.Entry(frameIncome, textvariable=userIncome, width=9)
    incomeEntry.pack(side="left", padx=10)

    debtLabel = tk.Label(frameDebt, text="DEBT: ", padx=10, pady=10, bg="grey", fg="black")
    debtLabel.pack(side="left", anchor="e")
    debtEntry = tk.Entry(frameDebt, width=10, textvariable=userDebt)
    debtEntry.pack(side="left", padx=10)

    savingsLabel = tk.Label(frameSavings, text="SAVINGS: ", padx=10, pady=10, bg="grey", fg="black")
    savingsLabel.pack(side="left", anchor="e")
    savingsEntry = tk.Entry(frameSavings, width=10, textvariable=userSavings)
    savingsEntry.pack(side="left", padx=10)

    expensesLabel = tk.Label(frameExpenses, text="EXPENSES: ", padx=10, pady=10, bg="grey", fg="black")
    expensesLabel.pack(side="left", anchor="e")
    expensesEntry = tk.Entry(frameExpenses, width=10, textvariable=userExpenses)
    expensesEntry.pack(side="left", padx=10)

    buttonSubmit = tk.Button(frameButtons, text="Submit", bg="black", fg= "white")
    buttonSubmit.pack(side="left", padx=10)
    buttonQuit = tk.Button(frameButtons, text ="Quit", bg = "red", fg="white", command=root.destroy)
    buttonQuit.pack(side="left", padx=100)

    nameEntry.insert(0, "Enter Your Name")


    root.mainloop()

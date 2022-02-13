import time
import tkinter as tk
from tkinter import ttk

def percentageOf(rate, total):
    return int((rate*total)/100)

userName = 0
userAge = 0
userIncome = 0
userDebt = 0
userSavings = 0
userExpenses = 0

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

    frameOutput = tk.Frame(root)
    frameOutput.pack(side = "top", anchor="w", padx=55, pady=20)

    outputLabel = tk.Label(frameOutput, font=20, padx=10, pady=5, bg="white", fg="red")
    outputLabel.pack(side="left")

    def backendMain():
        if (userAge.get() <= 14):
            if (userDebt.get() > 0):
                finalIncome = userIncome.get() - userDebt.get()
                if (finalIncome <= 0):
                    finalIncome += userSavings.get()
                    if (finalIncome <= 0):
                        outputLabel.config(text=
                                           "Hello there,{}, It's wise for you to settle your previous debts first".format(
                                               userName.get()))
                    else:
                        amountStocks = 0
                        amountBonds = percentageOf(5, finalIncome)
                        amountCrypto = 0
                        amountFD = percentageOf(60, finalIncome)
                        amountSavings = percentageOf(20, finalIncome)
                        amountExpenses = percentageOf(15, finalIncome)
                        outputLabel.config(text=
                        "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                        "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                            userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings, amountExpenses))
                else:
                    amountStocks = 0
                    amountBonds = percentageOf(5, finalIncome)
                    amountCrypto = 0
                    amountFD = percentageOf(60, finalIncome)
                    amountSavings = percentageOf(20, finalIncome)
                    amountExpenses = percentageOf(15, finalIncome)
                    outputLabel.config(text=
                    "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                    "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                        userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings,
                        amountExpenses))
        elif (userAge.get() > 14 and userAge.get() < 18):
            if (userDebt.get() > 0):
                finalIncome = userIncome.get() - userDebt.get()
                if (finalIncome <= 0):
                    finalIncome += userSavings.get()
                    if (finalIncome <= 0):
                        outputLabel.config(text=
                            "Hello there,{}, It's wise for you to settle your previous debts first".format(userName.get()))
                    else:
                        amountStocks = percentageOf(10, finalIncome)
                        amountBonds = percentageOf(25, finalIncome)
                        amountCrypto = percentageOf(5, finalIncome)
                        amountFD = percentageOf(25, finalIncome)
                        amountSavings = percentageOf(20, finalIncome)
                        amountExpenses = percentageOf(15, finalIncome)
                        outputLabel.config(text=
                        "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                        "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                            userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings, amountExpenses))
                else:
                    amountStocks = percentageOf(10, finalIncome)
                    amountBonds = percentageOf(25, finalIncome)
                    amountCrypto = percentageOf(5, finalIncome)
                    amountFD = percentageOf(25, finalIncome)
                    amountSavings = percentageOf(20, finalIncome)
                    amountExpenses = percentageOf(15, finalIncome)
                    outputLabel.config(text=
                    "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                    "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                        userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings,
                        amountExpenses))
        elif (userAge.get() >= 18 and userAge.get() <= 28):
            if (userDebt.get() > 0):
                finalIncome = userIncome.get() - userDebt.get()
                if (finalIncome <= 0):
                    finalIncome += userSavings.get()
                    if (finalIncome <= 0):
                        outputLabel.config(text=
                            "Hello there,{}, It's wise for you to settle your previous debts first".format(userName.get()))
                    else:
                        amountStocks = percentageOf(30, finalIncome)
                        amountBonds = percentageOf(25, finalIncome)
                        amountCrypto = percentageOf(15, finalIncome)
                        amountFD = percentageOf(15, finalIncome)
                        amountSavings = percentageOf(5, finalIncome)
                        amountExpenses = percentageOf(10, finalIncome)
                        outputLabel.config(text=
                        "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                        "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                            userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings, amountExpenses))
                else:
                    amountStocks = percentageOf(30, finalIncome)
                    amountBonds = percentageOf(25, finalIncome)
                    amountCrypto = percentageOf(15, finalIncome)
                    amountFD = percentageOf(15, finalIncome)
                    amountSavings = percentageOf(5, finalIncome)
                    amountExpenses = percentageOf(10, finalIncome)
                    outputLabel.config(text=
                    "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                    "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                        userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings,
                        amountExpenses))
        elif (userAge.get() > 28 and userAge.get() <= 50):
            if (userDebt.get() > 0):
                finalIncome = userIncome.get() - userDebt.get()
                if (finalIncome <= 0):
                    finalIncome += userSavings.get()
                    if (finalIncome <= 0):
                        outputLabel.config(text=
                            "Hello there,{}, It's wise for you to settle your previous debts first".format(userName.get()))
                    else:
                        amountStocks = percentageOf(25, finalIncome)
                        amountBonds = percentageOf(30, finalIncome)
                        amountCrypto = percentageOf(10, finalIncome)
                        amountFD = percentageOf(15, finalIncome)
                        amountSavings = percentageOf(10, finalIncome)
                        amountExpenses = percentageOf(10, finalIncome)
                        outputLabel.config(text=
                        "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                        "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                            userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings, amountExpenses))
                else:
                    amountStocks = percentageOf(25, finalIncome)
                    amountBonds = percentageOf(30, finalIncome)
                    amountCrypto = percentageOf(10, finalIncome)
                    amountFD = percentageOf(15, finalIncome)
                    amountSavings = percentageOf(10, finalIncome)
                    amountExpenses = percentageOf(10, finalIncome)
                    outputLabel.config(text=
                    "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                    "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                        userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings,
                        amountExpenses))
        elif (userAge.get() > 50 and userAge.get() <= 65):
            if (userDebt.get() > 0):
                finalIncome = userIncome.get() - userDebt.get()
                if (finalIncome <= 0):
                    finalIncome += userSavings.get()
                    if (finalIncome <= 0):
                        outputLabel.config(text=
                            "Hello there,{}, It's wise for you to settle your previous debts first".format(userName.get()))
                    else:
                        amountStocks = percentageOf(15, finalIncome)
                        amountBonds = percentageOf(20, finalIncome)
                        amountCrypto = percentageOf(5, finalIncome)
                        amountFD = percentageOf(40, finalIncome)
                        amountSavings = percentageOf(5, finalIncome)
                        amountExpenses = percentageOf(15, finalIncome)
                        outputLabel.config(text=
                        "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                        "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                            userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings, amountExpenses))
                else:
                    amountStocks = percentageOf(15, finalIncome)
                    amountBonds = percentageOf(20, finalIncome)
                    amountCrypto = percentageOf(5, finalIncome)
                    amountFD = percentageOf(40, finalIncome)
                    amountSavings = percentageOf(5, finalIncome)
                    amountExpenses = percentageOf(15, finalIncome)
                    outputLabel.config(text=
                    "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                    "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                        userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings,
                        amountExpenses))
        elif (userAge.get() > 65):
            if (userDebt.get() > 0):
                finalIncome = userIncome.get() - userDebt.get()
                if (finalIncome <= 0):
                    finalIncome += userSavings.get()
                    if (finalIncome <= 0):
                        outputLabel.config(text=
                            "Hello there,{}, It's wise for you to settle your previous debts first".format(userName.get()))
                    else:
                        amountStocks = percentageOf(10, finalIncome)
                        amountBonds = percentageOf(15, finalIncome)
                        amountCrypto = percentageOf(0, finalIncome)
                        amountFD = percentageOf(35, finalIncome)
                        amountSavings = percentageOf(20, finalIncome)
                        amountExpenses = percentageOf(20, finalIncome)
                        outputLabel.config(text=
                        "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                        "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                            userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings, amountExpenses))
                else:
                    amountStocks = percentageOf(10, finalIncome)
                    amountBonds = percentageOf(15, finalIncome)
                    amountCrypto = percentageOf(0, finalIncome)
                    amountFD = percentageOf(35, finalIncome)
                    amountSavings = percentageOf(20, finalIncome)
                    amountExpenses = percentageOf(20, finalIncome)
                    outputLabel.config(text=
                    "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\n"
                    "You should invest Rs.{} in Stocks, Rs.{} in secured Bonds, Rs.{} in Crypto, Rs.{} in Fixed Deposits, put Rs.{} in Savings Account and Rs.{} to spend".format(
                        userName.get(), amountStocks, amountBonds, amountCrypto, amountFD, amountSavings,
                        amountExpenses))

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

    buttonSubmit = tk.Button(frameButtons, text="Submit", bg="black", fg= "white", command=backendMain)
    buttonSubmit.pack(side="left", padx=10)
    buttonQuit = tk.Button(frameButtons, text ="Quit", bg = "red", fg="white", command=root.destroy)
    buttonQuit.pack(side="left", padx=100)

    nameEntry.insert(0, "Enter Your Name")


    root.mainloop()

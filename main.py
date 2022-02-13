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

    def backendMainWrapper():
        backendMain(userName, userAge, userIncome, userDebt, userSavings, userExpenses)


    def backendMain(name, age, income, debt, savings, expenses):
        userNameB = name
        userAgeB = age
        userIncomeB = income
        userDebtB = debt
        userSavingsB = savings
        userExpensesB = expenses

        if (userAgeB.get() <= 14):
            if (userDebtB.get() > 0):
                finalIncome = userIncomeB.get() - userDebtB.get()
                if (finalIncome <= 0):
                    finalIncome += userSavingsB.get()
                    if (finalIncome <= 0):
                        #text.config(state="normal")
                        #text.insert(
                         #   "Hello there,{}, We are here with a complete roadmap to your financial security and integrity\nYou should invest {} in Stocks,"
                          #  " {} in secured Bonds, {} in Crypto, {} in Fixed Deposits, put {} in Savings Account and {} to spend".format(
                           #     userNameB, 0, 0, 0, 0, 0, 0))
                        #text.config(state="disabled")
                        print("dfs")
                    else:
                        amountStocks = 0
                        amountBonds = percentageOf(5, finalIncome)
                        amountCrypto = 0
                        amountFD = percentageOf(60, finalIncome)
                        amountSavings = percentageOf(20, finalIncome)
                        amountExpenses = percentageOf(15, finalIncome)
                else:
                    amountStocks = 0
                    amountBonds = percentageOf(5, finalIncome)
                    amountCrypto = 0
                    amountFD = percentageOf(60, finalIncome)
                    amountSavings = percentageOf(20, finalIncome)
                    amountExpenses = percentageOf(15, finalIncome)
        elif (userAgeB > 14 and userAgeB < 18):
            x = 0  # code to be defined
        elif (userAgeB >= 18 and userAgeB <= 28):
            x = 0  # code to be defined
        elif (userAgeB > 28 and userAgeB <= 50):
            x = 0  # code to be defined
        elif (userAgeB > 50 and userAgeB <= 65):
            x = 0  # code to be defined
        elif (userAgeB > 65):
            x = 0  # code to be defined

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

    buttonSubmit = tk.Button(frameButtons, text="Submit", bg="black", fg= "white", command=backendMainWrapper)
    buttonSubmit.pack(side="left", padx=10)
    buttonQuit = tk.Button(frameButtons, text ="Quit", bg = "red", fg="white", command=root.destroy)
    buttonQuit.pack(side="left", padx=100)

    #outputLabel = tk.Label(frameOutput, text="dfas", padx=10, pady=5, bg="white", fg="red")
    #outputLabel.pack(side="left")
    #textOutput = tk.Text(frameOutput, padx =10, pady=5, bg="white", fg = "yellow", height=5, state="disabled")
    #textOutput.pack(side="left")

    nameEntry.insert(0, "Enter Your Name")


    root.mainloop()

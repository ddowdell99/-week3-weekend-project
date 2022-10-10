
class calculateROI():

    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.cashflow = {}
        self.cashOnCashROI = {}

    def caclculateIncome(self):

        def rentalIncome():
            self.rentalIncome = input('\nWhat is your monthly rental income? ')
            if self.rentalIncome.isdigit():
                self.income['Rental Income'] = int(self.rentalIncome)
            else:
                print('\nInvalid input! Please enter a number.')
                rentalIncome()
        rentalIncome()

        def otherIncome():
            enteringIncome = True
            while enteringIncome:
                incomeType = input('\nWhat other income would you like to report? (Laundry Income, Storage Income, etc... or "Done" (MAY HAVE TO ENTER MORE THAN ONCE) to finish and show current income!) ')
                if incomeType in self.income:
                    print(f'\nYou have already entered income for {incomeType}')
                    changeIncome = input("Would you like to change the income amount? (Y/N) ")
                    if changeIncome.lower() == 'y':
                        def changeIncomeValues():
                            changeIncomeValue = input('What would you like new income amount to be? ')
                            if changeIncomeValue.isdigit():
                                self.income[incomeType] = int(changeIncomeValue)
                            else:
                                print('Invalid Input! Please enter a number!')
                                changeIncomeValues()
                        changeIncomeValues()
                    elif changeIncome.lower() == 'n':
                        otherIncome()
                    else:
                        print('\nInvalid Input.')
                elif incomeType.lower() == 'done':
                    return
                elif incomeType.lower() != 'done':
                    incomeAmount = input('What is the approximate monthly income this would generate? ')
                    if incomeType.isdigit() == False and incomeAmount.isdigit() == True:
                        self.income[incomeType] = int(incomeAmount)
                    else:
                        print('\nPlease enter a valid income type and income amount to proceed!')
                        otherIncome()
        otherIncome()
        print('\nFinal Income:')
        self.income['Total Monthly Income'] = sum(self.income.values())
        for ft, fa in self.income.items():
            print(f'{ft.upper()} = ${fa}')
        return self.income['Total Monthly Income']

    def calculateExpenses(self):

        def taxExpense():
            self.tax = input('\nWhat is your monthly tax expense? ')
            if self.tax.isdigit():
                self.expenses['Taxes'] = int(self.tax)
            else:
                print('\nInvalid input! Please enter a number.')
                taxExpense()
        taxExpense()

        def insuranceExpense():
            self.insuranceExpense = input('What is your monthly insurance expense? ')
            if self.insuranceExpense.isdigit():
                self.expenses['Insurance Expense'] = int(self.insuranceExpense)
            else:
                print('Invalid input! Please enter a number.')
                insuranceExpense()
        insuranceExpense() 
        
        def utilitiesExpense():
            self.utilitiesExpense = input('What is your monthly utilities expense? ')
            if self.utilitiesExpense.isdigit():
                self.expenses['Utilities Expense'] = int(self.utilitiesExpense)
            else:
                print('Invalid input! Please enter a number.')
                utilitiesExpense()
        utilitiesExpense()         

        def otherExpenses():              
            enteringExpenses = True
            while enteringExpenses:
                expenseType = input('\nWhat other expense would you like to enter? (Enter "Done" (MAY HAVE TO ENTER MORE THAN ONCE) when finished): ')
                if expenseType in self.expenses:
                    print(f'You have already entered an expense for {expenseType}')
                    changeExpense = input("Would you like to change the expense amount? (Y/N) ")
                    if changeExpense.lower() == 'y':
                        def changeExpenseValue():
                            changeExpenseValue = input('What would you like new expense amount to be? ')
                            if changeExpenseValue.isdigit():
                                self.expenses[expenseType] = int(changeExpenseValue)
                            else:
                                print('Invalid Input! Please enter a number!')
                                self.changeExpenseValue()
                        changeExpenseValue()
                    elif changeExpense.lower() == 'n':
                        otherExpenses()
                if expenseType.lower() == 'done':
                    return
                if expenseType.lower() != 'done':
                    expenseAmount = input("What is the approximate monthly expense amount for this expense? ")
                if expenseAmount.lower() == 'done':
                    return
                elif expenseType.isdigit() == False and expenseAmount.isdigit() == True:
                    self.expenses[expenseType] = int(expenseAmount)
                else:
                    print('\nPlease enter a valid expense type and expense amount to proceed!')
                    otherExpenses()
        otherExpenses()
        print('\nFinal Expenses:')
        self.expenses['Total Monthly Expenses'] = sum(self.expenses.values())
        for fet, fea in self.expenses.items():
            print(f'{fet.upper()} = ${fea}')
        return self.expenses['Total Monthly Expenses']                

    def calculateCashFlow(self):
        income = self.income['Total Monthly Income']
        expenses = self.expenses['Total Monthly Expenses']
        self.cashflow['Total Monthly Cashflow'] = int(income - expenses)
        print('\nFinal CashFlow:')
        print(f'Total Monthly Income (${income}) - Total Monthly Expenses (${expenses}) =',end=' ')
        for fcf, fcfa in self.cashflow.items():
            print(f'{fcf.title()} = ${fcfa}')
        return self.cashflow['Total Monthly Cashflow']

    def calculateInvestment(self):

        def downPayment():
            self.downPayment = input('\nWhat was your down payment on this rental property? ')
            if self.downPayment.isdigit():
                self.cashOnCashROI['Down Payment'] = int(self.downPayment)
            else:
                print('Invalid input! Please enter a number.')
                downPayment()
        downPayment()

        def closingCosts():
            self.closingCosts = input('What were your closing costs? ')
            if self.closingCosts.isdigit():
                self.cashOnCashROI['Closing Costs'] = int(self.closingCosts)
            else:
                print('Invalid input! Please enter a number.')
                closingCosts()
        closingCosts()

        def repairBudget():
            self.repairBudget = input('What is your repair budget? ')
            if self.repairBudget.isdigit():
                self.cashOnCashROI['Repair Budget'] = int(self.repairBudget)
            else:
                print('Invalid input! Please enter a number.')
                repairBudget()
        repairBudget()
        
        def miscBudgets():
            enteringMisc = True
            while enteringMisc:
                respMiscBudget1 = input('Do you have any other budgets? (Y/N) **MAY HAVE TO ENTER "N" MORE THAN ONCE**: ')
                if respMiscBudget1.lower() == 'y':
                    self.miscBudgetType = input('What other budgets do you have? ')
                    self.miscBudgetAmount = input('How much per month is this budget? ')
                    if self.miscBudgetType.isdigit() == False and self.miscBudgetAmount.isdigit():
                        self.cashOnCashROI[self.miscBudgetType] = int(self.miscBudgetAmount)
                        miscBudgets()
                    else:
                        print('Invalid input! Please enter a number.')
                        miscBudgets()                
                elif respMiscBudget1.lower() == 'n':
                    return
        miscBudgets()

        print('\nTotal Investment:')
        self.cashOnCashROI['Total Investment'] = sum(self.cashOnCashROI.values())
        for fcoct, fcoca in self.cashOnCashROI.items():
            print(f'{fcoct.upper()} = ${fcoca}')
        return self.cashOnCashROI['Total Investment']  

    def yearlyCashFlow(self):
        yearlyCashFlow = self.cashflow['Total Monthly Cashflow'] * 12
        self.cashOnCashROI['Total Yearly Cashflow'] = int(yearlyCashFlow)

    def cashonCashROI(self):
        yearlyCashFlow = self.cashOnCashROI['Total Yearly Cashflow']
        totalInvestments = self.cashOnCashROI['Total Investment']
        cashOnCashROI = (yearlyCashFlow / totalInvestments) * 100
        self.cashOnCashROI['Cash on Cash ROI'] = cashOnCashROI
        print(f'Cash on Cash ROI = Yearly Cash Flows (${yearlyCashFlow}) / Total Investments (${totalInvestments})')
        print(f'\nYour Cash on Cash ROI is {cashOnCashROI}%')

# ----------- Main Program --------------- #

    def calculateCashOnCashROI(self):
        print("\nLet's figure out your Cash on Cash ROI!")
        print('First we need to collect your monthly income!')
        self.caclculateIncome()
        print('\nNext, we want to figure out your monthly expenses!')
        self.calculateExpenses()
        print('\nWe will now calculate your monthly cash flows!')
        self.calculateCashFlow()
        print("\nLastly, let's calculate your investment into this rental property!")
        self.calculateInvestment()
        self.yearlyCashFlow()
        print("\nCalculating Cash on Cash ROI...")
        self.cashonCashROI()
        def replay():
            replayResp = input('\nThank you for trying out this program! Would you like to run it again? (Y/N) ')
            if replayResp.lower() == 'y':
                print('\nRestarting Program...')
                self.calculateCashOnCashROI()
            elif replayResp.lower() == 'n':
                print('\nGoodbye!')
                return
            else:
                print('\nInvalid Input! Please enter either "Y" or "N"')
                replay()
        replay()


duplex = calculateROI()

duplex.calculateCashOnCashROI()





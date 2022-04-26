expenses=[]

def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month==month:
            print(f'{expense_amount}-{expense_type}')

def show_stats(month):
    total_amount_this_month=sum( expense_amount for expense_amount, _,expense_month in expenses if expense_month ==month)
    total_amount_all = sum( expense_amount for expense_amount, _, _ in expenses )
    number_of_expenses_this_month = sum(1 for expense_amount, _, _ in expenses)
    average_expenses_this_month=total_amount_this_month/number_of_expenses_this_month
    average_expenses_all=total_amount_all/len(expenses)

    print()
    print("statystyka")
    print("wszystkie wydatki w tym miesiący ",total_amount_this_month)
    print("sredni wydatek w tym miesiącu", average_expenses_this_month)
    print("wszyskie wydatki ",total_amount_all)
    print("średni wydatek ",average_expenses_all)



def add_expense(month):
    print()
    expense_amount=int(input("podaj kwote zł: "))
    expense_type=input("podaj typ wydatku, jedzenie, rozrywka, dom, inny")

    expense= (expense_amount,expense_type,month)
    expenses.append(expense)

while True:
    print ()
    month=int(input("wybierz miesiąc[1-12]: "))

    if month ==0:
        break

    while True:
        print()
        print("0. powrót do wyboru ")
        print ("1. wyświetl wszystkie wydatki")
        print ("2. dodaj wydatek")
        print("3. ststystyka ")
        choice=int(input("wybierz opcję: "))

        if choice == 0:
            break

        if choice == 1:
                show_expenses(month)


        if choice==2:
                add_expense(month)
        if choice==3:
             show_stats(month)

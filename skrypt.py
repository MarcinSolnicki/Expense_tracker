expenses = []

def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')

def add_expense(month):
    print()
    lista_wydatków=["jedzenie","rozrywka","dom","inny"]
    expense_amount = int(input("Podaj kwotę [zł]: "))
    
    for x in lista_wydatków:
        print(x)
    expense_type = input("Podaj typ wydatku  ")
    expense = (expense_amount, expense_type, month)
    expenses.append(expense)

def check_month(month):
   if (month<1 or month>12) :
       print("kaszanka zły miesiąc, wybierz 0") 

def check_type_expense(lista_wydatkow,expense_type):
    for x in lista_wydatkow:
        if x==expense_type:
            print("jest git")

def show_stats(month):
    total_amount_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
    average_expense_this_month = total_amount_this_month / number_of_expenses_this_month

    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
    average_expense_all = total_amount_all / len(expenses)

    print()
    print("Statystyki")
    print("Wszystkie wydatki w tym miesiącu [zł]:", total_amount_this_month)
    print("Średni wydatek w tym miesiącu [zł]: ", average_expense_this_month)
    print("Wszystkie wydatki [zł]:", total_amount_all)
    print("Średni wydatek [zł]: ", average_expense_all)

while True:
    try:
        month = int(input("Wybierz miesiąc [1-12]: "))
    except:
        print("wpisz liczbę baranie")
        month = int(input("Wybierz miesiąc [1-12]: "))

    check_month(month)
    if month == 0:
        break

    while True:
        print()
        print("0. Powrót do wyboru miesiąca")
        print("1. Wyświetl wszystkie wydatki")
        print("2. Dodaj wydatek")
        print("3. Statystyki")
        choice = int(input("Wybierz opcję: "))

        if choice == 0:
            break

        if choice == 1:
            show_expenses(month)

        if choice == 2:
            add_expense(month)
            check_type_expense

        if choice == 3:
            wiadomosc=show_stats(month)
            file=open("nowy.txt","w")
            print(show_stats(month),file=file)
            file.close()

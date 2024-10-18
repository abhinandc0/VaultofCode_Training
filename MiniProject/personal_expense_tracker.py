import csv
import os.path

expenses = []

def get_expense():
    print("Enter Expense ")
    date = input("Enter the date(DD-MM-YYYY): ")
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    categories = ["food", "Home", "Work", "Entertainment", "Misc"]
    while True:
        print("Select category below: ")
        for i, category_name in enumerate(categories):
            print(f" { i + 1 }. {category_name}")
        index_range = f"[1 - {len(categories)}]"
        index = int(input(f"Enter category number {index_range}: "))

        if index in range(0,len(categories)+1):
            selected_category = categories[index-1]
            expenses.append({'date': date,
                             'name': name,
                             'category': selected_category,
                             'amount': amount})
            return expenses
        else:
            print("Invalid category, try again.")
        break

def save_expense(expense,file_path):
    print(f"Saving expense: {expense} to {file_path}")
    file_exists = os.path.isfile(file_path) and os.path.getsize(file_path) > 0

    with open(file_path,"a",newline='') as file:
        field_name = ["date","name","category","amount"]
        writer = csv.DictWriter(file,fieldnames=field_name)
        #write header
        if not file_exists:
            writer.writeheader()
        #Write rows
        writer.writerows(expenses)


def load_expenses(file_path):
    try:
        with open(file_path,'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []



def summarize_expense(file_path):
    print("Summarizing expenses: ")
    expenses = load_expenses(file_path)

    total_spending = sum(float(expense["amount"]) for expense in expenses)
    print(total_spending)

    categories = set(expense["category"] for expense in expenses)
    for category in categories:
        category_spending = sum(float(expense["amount"])for expense in expenses if expense["category"] == category)
        print(f"{category} spending: {category_spending: .2f}")

    dates = set(expense["date"] for expense in expenses)
    for date in dates:
        daily_spending = sum(float(expense["amount"]) for expense in expenses if expense["date"] == date)
        print(f"{date} spending: {daily_spending: .2f}")


#function to delete expense
def delete_expense(file_path):
    date = input("Enter date of expense to delete (DD-MM-YYYY): ")
    name = input("Enter name of the expense to delete: ")

    expenses = load_expenses(file_path)
    expenses = [expense for expense in expenses if not (expense["date"] == date and expense["name"] == name)]
    with open(file_path,'w', newline='') as file :
        field_names = ["date", "name","category","amount"]
        writer = csv.DictWriter(file,fieldnames=field_names)
        writer.writeheader()
        writer.writerows(expenses)

    print("Expense deleted successfully!")


def main():
    print("Expense tracker")
    file_path = "expenses.csv"

    while True:
        print(f"1. Add Expense\n"
              f"2. View summary\n"
              f"3. Delete Expense\n"
              f"4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            #getting expense from user
            expense = get_expense()

            #save user input
            save_expense(expense,file_path)

        elif choice == "2":
            #summarize all expenses from csv file
            summarize_expense(file_path)

        elif choice == "3":
            #Delete expense
            delete_expense(file_path)

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()


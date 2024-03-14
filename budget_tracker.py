# Function to add an expense
def add_expense(transactions, category, amount):
    transactions['expenses'].append({'category': category, 'amount': amount})

# Function to add income
def add_income(transactions, category, amount):
    transactions['income'].append({'category': category, 'amount': amount})

# Function to calculate the remaining budget
def calculate_budget(transactions):
    total_income = sum(transaction['amount'] for transaction in transactions['income'])
    total_expenses = sum(transaction['amount'] for transaction in transactions['expenses'])
    return total_income - total_expenses

# Function to display budget summary
def display_summary(transactions):
    remaining_budget = calculate_budget(transactions)
    print(f"Remaining Budget: ${remaining_budget:.2f}")

# Main function to interact with users
def main():
    transactions = {'expenses': [], 'income': []}

    while True:
        print("\n1. Add Expense")
        print("2. Add Income")
        print("3. View Budget Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(transactions, category, amount)
            print("Expense added successfully.")

        elif choice == '2':
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            add_income(transactions, category, amount)
            print("Income added successfully.")

        elif choice == '3':
            display_summary(transactions)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__== "__main__":
    main()
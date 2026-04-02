def main():
    print("💰 Welcome to Bank Balance + Expense Tracker!")
    
    # Step 1: Ask for initial bank balance
    bank_balance = float(input("Enter your current bank balance: $"))
    
    # Expense categories
    expense_categories = {
        '🍔 Food': 0,
        '🚗 Transport': 0,
        '💡 Utilities': 0,
        '🍿 Entertainment': 0,
        '🩺 Healthcare': 0,
        'Other': 0
    }
    
    while True:
        print("\nSelect a category to add expense:")
        for i, category in enumerate(expense_categories.keys(), 1):
            print(f"{i}. {category}")
        print("0. Exit & Show Summary")

        choice = int(input("Enter choice: "))
        
        if choice == 0:
            break
        elif 1 <= choice <= len(expense_categories):
            category_name = list(expense_categories.keys())[choice - 1]
            amount = float(input(f"Enter amount spent on {category_name}: $"))
            
            if amount > bank_balance:
                print("⚠️ Not enough balance! Expense not added.")
            else:
                expense_categories[category_name] += amount
                bank_balance -= amount
                print(f"✅ Added ${amount:.2f} to {category_name}. Remaining balance: ${bank_balance:.2f}")
        else:
            print("❌ Invalid choice. Try again.")
    
    # Step 2: Show summary
    print("\n📊 Expense Summary:")
    total_spent = 0
    for category, spent in expense_categories.items():
        print(f"{category}: ${spent:.2f}")
        total_spent += spent
    
    print(f"\nTotal Spent: ${total_spent:.2f}")
    print(f"Remaining Balance: ${bank_balance:.2f}")
    print("🎉 Tracking complete!")


if __name__ == "__main__":
    main()

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
# calculate monthly savingd 
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings is {monthly_savings} sh")

# calculate projected annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your projected annual savings is {projected_savings}")
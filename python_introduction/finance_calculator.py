monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
# calculate monthly savingd 
monthly_savings = monthly_income - total_monthly_expenses
print(f"Your monthly savings is {monthly_savings} sh")

# calculate projected annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your projected annual savings is {projected_savings}")
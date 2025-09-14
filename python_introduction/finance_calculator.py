total_monthly_income = input("Enter your monthly income: ")
total_monthly_expenses = input("Enter your total monthly expenses: ")

monthly_savings = int(total_monthly_income) - int(total_monthly_expenses)
print("Your monthly savings is: ", monthly_savings)

projected_annual_savings = int(monthly_savings * 12 + (monthly_savings * 0.05 * 12))
print(f"Projected savings after one year, with interest, is: {projected_annual_savings}")
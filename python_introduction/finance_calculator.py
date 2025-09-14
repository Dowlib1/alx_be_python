total_monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = float(total_monthly_income) - float(total_monthly_expenses)
print("Your monthly savings is: ", monthly_savings)

projected_annual_savings = float(monthly_savings * 12 + float(monthly_savings * 0.05 * 12))
print(f"Projected savings after one year, with interest, is: {projected_annual_savings}")
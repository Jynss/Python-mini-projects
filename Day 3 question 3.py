savings = float(input("Enter your savings amount: "))
interest = int(input("Enter the interest rate: "))
total_years = int(input("Enter the number of years: "))
years = 1

while years <= total_years:
    total = savings * (1 + (interest / 100))**years
    print("Year ", str(years), str(round(total, 2)))
    years += 1

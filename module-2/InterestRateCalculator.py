Interest_rate = int(input("Please enter the interest rate as a whole number. For example if the rate is 8% then enter 8: "))
print()
Initial_investment = float(input("Please enter the initial investment as a whole number. For example if the initial investment is $10,000 then enter 10000: "))

def time_to_double(Interest_rate, Initial_investment):
    years = 0
    balance = Initial_investment
    while balance < 2 * Initial_investment:
        balance += balance * (Interest_rate / 100)
        years += 1
    return years

years_to_double = time_to_double(Interest_rate, Initial_investment)
print()

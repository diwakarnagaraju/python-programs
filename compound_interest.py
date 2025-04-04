# Calculate the compound interest for a given principal amount, interest rate, and time period

# the formula to calculate compund interest is A = P (1 + r/n)^(nt)

''' where
 A: Final amount (principal + interest)
P: Principal (initial investment)
r: Annual interest rate (as a decimal, e.g., 5% = 0.05)
n: Number of times interest is compounded per year (e.g., 12 for monthly)
t: Time in years '''

# The compound interest alone is then A – P. 

def compound(principal, rate, time, n):
    amount = principal * (1 + rate/n) ** (n * time)
    intrest = amount - principal
    return amount, intrest 

principal = 400000
rate = 0.12
time = 4 # years
n = 12 #months

final_amount , intrest = compound(principal, rate, time, n)

print(f"final_amount: {final_amount:.2f}")
print(f"intrest: {intrest:.2f}")


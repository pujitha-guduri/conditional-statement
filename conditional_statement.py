salary = float(input("Enter your salary: "))

if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = (salary - 250000) * 0.05
elif salary <= 1000000:
    tax = (250000 * 0.05) + (salary - 500000) * 0.07
else:
    tax = (250000 * 0.05) + (500000 * 0.07) + (salary - 1000000) * 0.10

print("Tax =", tax)
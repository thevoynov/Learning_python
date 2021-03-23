year = 0
while year <= 2021:
    year = int(year + 1)
    if (year % 4) == 0 and (year % 100) and (year % 400):
        print(year, "- год високосный.")
    else:
        print(year, "- год невисокосный.")
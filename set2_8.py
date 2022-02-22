rate = float(input('What is the pay rate (eg 700.50 which is 700 naira, 50 kobo)> '))
hours = int(input('Hours wordked during the week (digits only)> '))
total_pay = rate * hours
print(f'Total pay is {int(total_pay)} Naira, {round(total_pay - int(total_pay),2)} kobo ')
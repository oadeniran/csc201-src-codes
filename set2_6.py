print('''
    CALCULATE AREA OF WHICH SHAPE
    1. SQUARE
    2 TRIANGLE
    3 CIRCLE''')
a = input('option(input numbers) > ')
if a == '1':
    side = input('Input slength of side > ')
    print(int(side) ** 3)
elif a == '2':
    base = input('Input the base> ')
    height = input('Input the height> ')
    print(0.5 * int(base) * int(height))
elif a == '3':
    radius = input('Input radius> ')
    print(3.142 * int(radius)**2)
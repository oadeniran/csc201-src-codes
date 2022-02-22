import math
base = float(input('base > '))
while base <= 0:
    print('base must be postitive')
    base = float(input('base > '))

height = float(input('height > '))
while height <= 0:
    print('base must be postitive')
    height = int(input('height > '))

one_half = ((4*height**2) + base**2) ** 0.5
#print(one_half)
scnd_half = math.log((one_half + (2*height)) / base,10) * base**2 / (2*height)

#print(scnd_half)
l = one_half + scnd_half
print(round(l,2))
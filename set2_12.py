import math
def calc_cv(w = None, t = None):
    import math
    h = 6.626 * 10**-34
    k = 1.381 * 10**-23

    if w == None:
        w = float(input('frequency in cm^-1 > '))
        w *= 3 * 10**10

    if t == None: 
        t = float(input('Temperature in kelvin > '))

    #print(-h*w)
    #print(k*t)
    exp = math.exp(-(h*w)/(k*t))
    #print(exp)

    exp_denominator = (1 - exp) ** 2

    one_half = k * (((h*w )/ k*t) ** 2)
    cv = one_half  * (exp / exp_denominator)
    #print(cv)
    return cv

calc_cv()
molecules = {'c12':564.9,
             '02' : 1580.361,
             'HCL': 2989.74,
             'D2' : 3118.4,
             'H2' : 4395.2
}
for molecule in molecules.keys():
    print(f'Vibrational contribution of {molecule}')
    for t in range(100,2000,100):
        ans = calc_cv(molecules[molecule], t=t)
        print(str(t)+'k:',ans)
    print('end of cv for', molecule)




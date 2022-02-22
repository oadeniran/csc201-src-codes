
# Distance calculation
def dist(u,t,a):
    s =  u*t + 0.5*a*(t**2)
    return s

# effective resistance
def effct_rst():
    r = 0
    nums = []
    for i in range(4):
        a = input(f'Number {i} ')
        nums.append(a)
        inv = 1/int(a)
        r += inv
    return round(1/r)

#Period
def period(l):
    g = 9.8
    t = (2 * 3.142) * (l/g)**0.5
    return t

# perpendicular distance
def shortest_dist(x1,x2,y1,y2):
    d = (x1-x2)**0.5 + (y1-y2)**0.5
    return d

# Final velocity
def final_v_squared (u,a,s):
    v_sqr = u**2 + 2*a*s
    return v_sqr

# Sum of integers
def sum_ten_integers():
    nums = []
    for i in range(10):
        a = input(f'Number {i} ')
        nums.append(int(a))
    return sum(nums)

# Largest among ten numbers
def largest_among_ten_nums():
    b = 0
    nums = []
    for i in range(10):
        a = input(f'Number {i} ')
        nums.append(a)
        if int(a) > b:
            b = int(a)
    return b


# swap two numbers
def swap(x,y):
    a = x
    x = y
    y = x
    return x,y

# Average of 10 integernumbers
def average_of_ten_numbers():
    b = 0
    nums = []
    for i in range(10):
        a = input(f'Number {i} ')
        nums.append(a)
        b += int(a)
    
    return b / 10

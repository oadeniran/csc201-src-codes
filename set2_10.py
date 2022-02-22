def shortest_dist(x1,x2,y1,y2):
    d = (x1-x2)**2 + (y1-y2)**2
    return d**0.5

x1 = int(input('x1 > '))
y1 = int(input('y1 > '))
x2 = int(input('x2 > '))
y2 = int(input('y2 > '))

d = shortest_dist(x1,x2,y1,y2)
print(d)
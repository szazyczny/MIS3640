#Define a function quadratic(a, b, c) to solve a quadratic equation: ax^2+bx+c=0
#Discriminant: b^2−4ac

def quadratic(a, b, c):
    d = (b ** 2 - 4 * a * c) ** 0.5 #use discriminant, WHY ** 0.5?
    x = (-b + d) / (2 * a) #solving for x
    return x

print(quadratic(1, 6, 9))
print(quadratic(3, 4, 5))
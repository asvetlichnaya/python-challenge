def validate_triangle(a1: int, b1: int, c1: int):
    if a1 + b1 > c1 and a1 + c1 > b1 and c1 + b1 > a1:
        return print("It's a triangle")
    else:
        return print("It's not a triangle!")


a = input('a: ')
b = input('b: ')
c = input('c: ')
validate_triangle(a, b, c)


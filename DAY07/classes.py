# OOP - Programming Paradigm
# In OOP we think about world in terms of objects
# Objects might store information or support the ability todo some operations
# OOP helps you to create new types or you can say customized types e.g. 2D Values
# class = A templete for a type of objects


class point():
    # It'll called automaticly every time when creating a new point
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


inpt1 = input("Enter The value of X coordinate: ")
inpt2 = input("Enter The value of Y coordinate: ")
p = point(inpt1, inpt2)
print(f'the value of x coordinate is = {p.x}')
print(f'the value of y coordinate is = {p.y}')

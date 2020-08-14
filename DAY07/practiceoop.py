class Studentinfo():
    def __init__(self, name, dept, CGPA):
        self.name = name
        self.department = dept
        self.gpa = CGPA


nam = input("Enter you name: ")
dept = input("Department: ")
CG = input("Enter CGPA: ")
ID1 = Studentinfo(nam, dept, CG)
print(
    f'Info of ID1: \n Name:{ID1.name}\n Department:{ID1.department}\n CGPA:{ID1.gpa}')

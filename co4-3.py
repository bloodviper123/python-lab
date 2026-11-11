# co4-3

class rect:
    def __init__(self):
        self.__l = int(input("Enter the length of rectangle:"))
        self.__b = int(input("Enter the breadth of rectangle:"))
        
    def __lt__(ob1, ob2):
        area1=ob1.__l*ob1.__b
        area2=ob2.__l*ob2.__b
        print("Area of rectangle1=",area1)
        print("Area of rectangle2=",area2)
        return area1<area2
print("Enter the length and breadth of Rectangle1")
ob1=rect()
print("Enter the length and breadth of Rectangle2")
ob2=rect()
if(ob1<ob2):
    print("Rectangle1 is less than Rectangle2")
else:
    print("Rectangle2 is less than Rectangle1")

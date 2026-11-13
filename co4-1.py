#co4-1

class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        p=2*(self.l+self.b)
        print("Perimeter of rectangle is:",p)
    def compare(self,obj2):
        try:
            if obj1.area()==obj2.area():
                print("Both area are equal")
            elif obj1.area()>obj2.area():
                print("Area of rectangle1 is greater than rectangle2")
            elif obj1.area()<obj2.area():
                print("Area of rectangle2 is greater than rectangle1")
        except:
            print("Can't compare!")
l1=int(input("Enter the length of first rectangle:"))
b1=int(input("Enter the bredth of first rectangle:"))
l2=int(input("Enter the length of second rectangle:"))
b2=int(input("Enter the bredth of second rectangle:"))
obj1=Rectangle(l1,b1)
obj2=Rectangle(l2,b2)        
print("Area of rectangle1:",obj1.area())
print("Area of rectangle2:",obj2.area())
obj1.compare(obj2)
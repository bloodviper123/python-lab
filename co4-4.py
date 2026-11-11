# co4-4

class time:
    def __init__(self):
        self.__h= int(input("Enter the hour:"))
        self.__m = int(input("Enter the minute:"))
        self.__s = int(input("Enter the second:"))
    def __add__(tob1, tob2):
        hours=tob1.__h+tob2.__h
        print("Sum of hours=",hours)
        minutes=tob1.__m+tob2.__m
        print("Sum of minutes=",minutes)
        seconds=tob1.__s+tob2.__s
        print("Sum of seconds=",seconds)
        if hours>=24:
            hours=hours%24
        if minutes>=60:
            hours=hours+minutes//60
            minutes=minutes%60
        if seconds>=60:
            minutes=minutes+seconds//60
            seconds=seconds%60
        return hours,minutes,seconds
    
print("Enter first time")
tob1=time()
print("Enter second time")
tob2=time()
print("Sum of two times in (hours,minutes,seconds)=",tob1+tob2)

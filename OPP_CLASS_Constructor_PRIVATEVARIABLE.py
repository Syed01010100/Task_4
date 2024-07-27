#Task:-  OOP concept complete the below tasks
#(a) Create a python class called Circle with Constructor which will take a list as an argument. The list is [10, 501, 22, 37, 100, 999, 87, 351]
#(b) Create proper member variable inside the task if required and use them when necessary. For example for this task create a private class variable names pi=3.141.
#(c) From the given list create two class Methods Area and Perimeter. Use the methods to calculate the area and perimeter for the given list.

class Circle:
    __pi = 3.144 #private variable

    def __init__(self): # constructor
        self.list = [10, 501, 22, 37, 100, 999, 87, 351]

    def area(self):
        area_list = []
        for radius in self.list:
            area_circle = self.__pi * radius * radius
            area_list.append(area_circle)
        return area_list
    def disply(self): # display out
        return self.area()

    def perimeter(self):
        perimeter_list = []
        for radis in self.list:
            # iterate the list values and calulate perimeter
            perimeter_circle = 2 *self.__pi* radis
            perimeter_list.append(perimeter_circle)
            # append the perimeter values to new list
        return perimeter_list
    def disply1(self):
        return self.perimeter()
Object = Circle() #object
print("area:",Object.disply())
print("perimeter:",Object.disply1())
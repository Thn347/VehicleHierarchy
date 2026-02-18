'''
A tester class to run the neccessary classes
Author: Thuan Nguyen
'''

# from <file> import <class>
from manufacturer import Manufacturer

def main():
    # print("Hello World")
    # Manufacturer.print_me()
    m = Manufacturer("Ford", "USA")
    # m.print_me()
    # print(m._name)   #DO NOT access private variable
    print(m.get_name) 
    print(m.get_country)
    print(m)
    pass

if __name__ == "__main__":
    main()
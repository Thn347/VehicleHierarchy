'''
A tester class to run the neccessary classes
Author: Thuan Nguyen
'''

# from <file> import <class>
from manufacturer import Manufacturer
from auto_model import AutoModel

def main():
    # print("Hello World")
    # Manufacturer.print_me()
    # m = Manufacturer("Ford", "USA")
    # m.print_me()
    # print(m._name)   #DO NOT access private variable
    # print(m.get_name) 
    # print(m.get_country)
    # print(m)
    original_list = [2020, 2021]
    am = AutoModel("F150", True, original_list)

    print(am.get_years)

    original_list.clear()

    original_list.append(2022)

    print(am.get_years)
    # pass

if __name__ == "__main__":
    main()
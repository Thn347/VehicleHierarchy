'''
A tester class to run the neccessary classes
Author: Thuan Nguyen
'''

# from <file> import <class>
from manufacturer import Manufacturer
from auto_model import AutoModel
from sedan import Sedan

def main():
    s = Sedan(
        Manufacturer("Honda", "Japan"),
        AutoModel("Civic", False, [1996, 1997, 1998]),
        28.0
    )

if __name__ == "__main__":
    main()
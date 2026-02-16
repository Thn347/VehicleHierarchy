'''
This represented vehicle manufacturer
'''

class Manufacturer:
    """
    Docstring for Manufacturer
    """
    # constructor
    def __init__(self, name: str, country: str):
        self._name = name
        self._country = country
        pass

    # getters methods
    @property
    def get_name(self) -> str:
        return self._name
    
    # properties
    @property
    def get_country(self) -> str:
        return self._country
    
    def print_me(self):
        print("Hello Manufacturer")
    
    # setter methods

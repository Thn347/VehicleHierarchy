'''
This is the unit testing file.
Author: Thuan Nguyen
'''

import pytest

from manufacturer import Manufacturer
from auto_model import AutoModel

class TestManufacturer:
    def test_constructor(self):
        m = Manufacturer("Ford", "USA")
        assert m.get_name == "Ford"
        assert m.get_country == "USA"

    def test_constructor_2(self):
        m = Manufacturer("Honda", "Japan")
        assert m.get_name == "Honda"
        assert m.get_country == "Japan"

    def test_str(self):
        m = Manufacturer("BMW", "Germany")
        assert str(m) == "(BMW, Germany)"


class TestAutoModel:
    def test_constructor(self):
        am = AutoModel("F150", True, [2020, 2021, 2022])
        assert am.get_name == "F150"
        assert am.get_in_production == True
        assert am.get_years == [2020, 2021, 2022]

    def test_years_defensive_copy(self):
        original_list = [2020, 2021]
        am = AutoModel("F150", True, original_list)
        original_list.clear()
        assert am.get_years == [2020, 2021]

    # F150 in production = True, release year: 2020
    def test_str(self):
        am = AutoModel("F150", True, [2020, 2021, 2022])
        assert str(am) == "F150 in production = True,  release year: 2020"

    


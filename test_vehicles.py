'''
This is the unit testing file.
Author: Thuan Nguyen
'''

import pytest

from manufacturer import Manufacturer
from auto_model import AutoModel
from vehicle import Vehicle
from sedan import Sedan
from truck import Truck
# from garage import Garage


# ============================================================
#  Manufacturer tests
# ============================================================
class TestManufacturer:
    def test_constructor(self):
        m = Manufacturer("Ford", "USA")
        assert m.name == "Ford"
        assert m.country == "USA"

    def test_str(self):
        m = Manufacturer("BMW", "Germany")
        assert str(m) == "BMW, Germany"

    def test_constructor_2(self):
        m = Manufacturer("Honda", "Japan")
        assert m.name == "Honda"
        assert m.country == "Japan"
        assert str(m) == "Honda, Japan"

    
# ============================================================
#  AutoModel tests
# ============================================================
class TestAutoModel:
    def test_constructor(self):
        am = AutoModel("F150", True, [2020, 2021, 2022])
        assert am.name == "F150"
        assert am.in_production == True
        assert am.years == [2020, 2021, 2022]

    def test_first_year(self):
        am = AutoModel("Civic", False, [1996, 1997, 1998])
        assert am.first_year == 1996

    def test_str(self):
        am = AutoModel("Tundra", False, [1987, 1988])
        result = str(am)
        assert "Tundra" in result
        assert "False" in result
        assert "1987" in result

    def test_empty_years_raises(self):
        with pytest.raises(ValueError):
            AutoModel("Invisible Car", False, [])

    def test_years_defensive_copy(self):
        """Changing the original must not affect the model"""
        original_list = [2020, 2021]
        am = AutoModel("F150", True, original_list)
        original_list.clear()
        assert am.years == [2020, 2021]

    def test_years_getter_returns_copy(self):
        """Changing the original must not affect the model"""
        am = AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018])
        returned = am.years
        returned.append(2019)
        assert len(am.years) == 4


# ============================================================
#  Vehicle / abstract contract tests
# ============================================================
class TestVehicleAbstract:
    def test_vehicle_cannot_be_directly_initialized(self):
        """Vehicle is abstract and should not be directly initialized"""
        with pytest.raises(TypeError):
            Vehicle(
                Manufacturer("Xavier", "Yelan"),
                AutoModel("Zhongli", True, [2025]),
                25.0
            )

    def test_subclass_must_implement_number_of_wheels(self):
        """A subclass that does not have number_of_wheels should not work"""
        # This incomplete version should raise TypeError
        with pytest.raises(TypeError):
            class Incompletion(Vehicle):
                pass
            Incompletion(
                Manufacturer("Xavier", "Yelan"),
                AutoModel("Zhongli", True, [2025]),
                30.0
            )


# ============================================================
#  Sedan tests
# ============================================================
class TestM3Limited:
    @pytest.fixture
    def m3(self):
        return Sedan(
            Manufacturer("BMW", "Germany"),
            AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018]),
            30.0,
        )
    
    def test_number_of_wheels(self, m3):
        assert m3.number_of_wheels() == 4

    def test_release_year(self, m3):
        assert m3.release_year == 2015

    def test_mpg(self, m3):
        assert m3.mpg == pytest.approx(30.0)

    def test_manufacturer(self, m3):
        assert m3.manufacturer.name == "BMW"
        assert m3.manufacturer.country == "Germany"

    def test_model_name(self, m3):
        assert m3.model.name == "M3 Limited"

    def test_how_far_with(self, m3):
        assert m3.how_far_with(10) == pytest.approx(300.0)
        assert m3.how_far_with(5) == pytest.approx(150.0)

    def test_str_contains_required_parts(self, m3):
        s = str(m3)
        assert "(BMW, Germany)" in s
        assert "M3 Limited" in s
        assert "30.00" in s

    def test_str_does_not_contain_dually(self, m3):
        s = str(m3)
        assert "dually" not in s.lower()

    def test_is_instance_of_vehicle(self, m3):
        assert isinstance(m3, Vehicle)
 

# ============================================================
#  Truck tests
# ============================================================
class TestTruck:
    @pytest.fixture
    def f150(self):
        return Truck(
            Manufacturer("Ford", "USA"),
            AutoModel("F150", True, [2020, 2021, 2022]),
            20.0,
        )

    @pytest.fixture
    def tundra(self):
        return Truck(
            Manufacturer("Toyota", "Japan"),
            AutoModel("Tundra", False, [1987, 1988]),
            30.0,
            is_dually=True,
        )

    # not dually
    def test_default_not_dually(self, f150):
        assert f150.is_dually is False

    def test_wheels_non_dually(self, f150):
        assert f150.number_of_wheels() == 4

    def test_release_year_f150(self, f150):
        assert f150.release_year == 2020

    def test_str_non_dually(self, f150):
        s = str(f150)
        assert "(Ford, USA)" in s
        assert "F150" in s
        assert "20.00" in s
        assert "False" in s

    # dually
    def test_is_dually_true(self, tundra):
        assert tundra.is_dually is True

    def test_wheels_dually(self, tundra):
        assert tundra.number_of_wheels() == 6

    def test_release_year_tundra(self, tundra):
        assert tundra.release_year == 1987

    def test_str_dually(self, tundra):
        s = str(tundra)
        assert "(Toyota, Japan)" in s
        assert "Tundra" in s
        assert "30.00" in s
        assert "True" in s

    def test_how_far_with(self, tundra):
        assert tundra.how_far_with(6) == pytest.approx(180.0)

    def test_is_instance_of_vehicle(self, f150):
        assert isinstance(f150, Vehicle)


# ============================================================
#  Comparable / ordering tests for Vehicle
# ============================================================
class TestVehicleComparison:
    @pytest.fixture
    def sedan_1996(self):
        return Sedan(
            Manufacturer("Honda", "Japan"),
            AutoModel("Civic", False, [1996, 1997, 1998]),
            28.0,
        )
    
    @pytest.fixture
    def truck_1996(self):
        return Truck(
            Manufacturer("Chevy", "USA"),
            AutoModel("Silverado", False, [1996, 1997, 1998, 1999, 1920]),
            18.0,
        )
    
    @pytest.fixture
    def sedan_2015(self):
        return Sedan(
            Manufacturer("BMW", "Germany"),
            AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018]),
            30.0,
        )

    @pytest.fixture
    def truck_2020(self):
        return Truck(
            Manufacturer("Ford", "USA"),
            AutoModel("F150", True, [2020, 2021, 2022]),
            20.0,
        )

    def test_lt(self, sedan_1996, sedan_2015):
        assert sedan_1996 < sedan_2015

    def test_not_lt_when_greater(self, sedan_2015, sedan_1996):
        assert not (sedan_2015 < sedan_1996)

    def test_eq_same_year(self, sedan_1996, truck_1996):
        assert sedan_1996 == truck_1996

    def test_not_eq_different_year(self, sedan_1996, sedan_2015):
        assert sedan_1996 != sedan_2015

    def test_gt(self, truck_2020, sedan_2015):
        assert truck_2020 > sedan_2015

    def test_sorted_order(self, sedan_1996, sedan_2015, truck_2020):
        vehicles = [truck_2020, sedan_1996, sedan_2015]
        result = sorted(vehicles)
        assert result[0].release_year == 1996
        assert result[1].release_year == 2015
        assert result[2].release_year == 2020
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
from garage import Garage


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


# ============================================================
#  Garage tests
# ============================================================
class TestGarage:
    @pytest.fixture
    def full_garage(self):
        g = Garage()
        g.add_vehicle(
            Truck(
                Manufacturer("Ford", "USA"),
                AutoModel("F150", True, [2020, 2021, 2022]),
                20.0,
            )
        )
        g.add_vehicle(
            Sedan(
                Manufacturer("Honda", "Japan"),
                AutoModel("Civic", False, [1996, 1997, 1998]),
                28.0,
            )
        )
        g.add_vehicle(
            Sedan(
                Manufacturer("BMW", "Germany"),
                AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018]),
                30.0,
            )
        )
        g.add_vehicle(
            Truck(
                Manufacturer("Toyota", "Japan"),
                AutoModel("Tundra", False, [1987, 1988]),
                30.0,
                is_dually=True,
            )
        )
        return g

    def test_add_vehicle(self):
        g = Garage()
        assert len(g.vehicles) == 0
        g.add_vehicle(
            Sedan(
                Manufacturer("ELLI", "China"),
                AutoModel("Offden", True, [2030]),
                25.0,
            )
        )
        assert len(g.vehicles) == 1

    def test_vehicles_returns_copy(self):
        """Changing the returned list should not have any affect"""
        g = Garage()
        g.add_vehicle(
            Sedan(
                Manufacturer("HoI", "Korea"),
                AutoModel("E051", True, [3001]),
                35.0,
            )
        )
        external = g.vehicles
        external.clear()
        assert len(g.vehicles) == 1

    def test_empty_garage(self):
        g = Garage()
        g.add_vehicle(
            Sedan(
                Manufacturer("Teyeto", "Vietnam"),
                AutoModel("Tempo", True, [2020]),
                25.0,
            )
        )
        g.empty_garage()
        assert len(g.vehicles) == 0

    def test_empty_garage_does_not_set_none(self):
        """After emptying, add_vehicle should still work (list not None)."""
        g = Garage()
        g.add_vehicle(
            Sedan(
                Manufacturer("Teyeto", "Vietnam"),
                AutoModel("Tempo", True, [2020]),
                25.0,
            )
        )
        g.empty_garage()
        # If the internal list were None, this would raise an AttributeError
        g.add_vehicle(
            Sedan(
                Manufacturer("X", "Y"),
                AutoModel("Z", False, [2021]),
                30.0,
            )
        )
        assert len(g.vehicles) == 1

    def test_sort_by_release_year(self, full_garage):
        full_garage.sort_by_release_year()
        vehicles = full_garage.vehicles
        years = [v.release_year for v in vehicles]
        assert years == sorted(years)

    def test_sort_order_specific(self, full_garage):
        full_garage.sort_by_release_year()
        vehicles = full_garage.vehicles
        assert vehicles[0].release_year == 1987
        assert vehicles[1].release_year == 1996
        assert vehicles[2].release_year == 2015
        assert vehicles[3].release_year == 2020

    def test_str_contains_all_vehicles(self, full_garage):
        s = str(full_garage)
        assert "F150" in s
        assert "Civic" in s
        assert "M3 Limited" in s
        assert "Tundra" in s

    def test_str_vehicles_on_separate_lines(self, full_garage):
        s = str(full_garage)
        lines = s.strip().split("\n")
        assert len(lines) == 4


# ============================================================
#  Integration / end-to-end test (Main)
# ============================================================
class TestIntegration:

    def test_full_workflow(self):
        """Mirrors the main.py scenario end-to-end."""
        ford = Manufacturer("Ford", "USA")
        honda = Manufacturer("Honda", "Japan")
        bmw = Manufacturer("BMW", "Germany")
        toyota = Manufacturer("Toyota", "Japan")

        f150 = Truck(ford, AutoModel("F150", True, [2020, 2021, 2022]), 20.0)
        civic = Sedan(honda, AutoModel("Civic", False, [1996, 1997, 1998]), 28.0)
        m3 = Sedan(bmw, AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018]), 30.0)
        tundra = Truck(toyota, AutoModel("Tundra", False, [1987, 1988]), 30.0, is_dually=True)

        g = Garage()
        for v in [f150, civic, m3, tundra]:
            g.add_vehicle(v)

        # Before sorting
        before = g.vehicles
        assert before[0].model.name == "F150"
        assert before[1].model.name == "Civic"
        assert before[2].model.name == "M3 Limited"
        assert before[3].model.name == "Tundra"

        g.sort_by_release_year()

        # After sorting
        after = g.vehicles
        assert after[0].model.name == "Tundra"
        assert after[1].model.name == "Civic"
        assert after[2].model.name == "M3 Limited"
        assert after[3].model.name == "F150"

        # Verify types survived polymorphism
        assert isinstance(after[0], Truck)
        assert isinstance(after[1], Sedan)
        assert isinstance(after[2], Sedan)
        assert isinstance(after[3], Truck)

        # Verify dually status
        assert after[0].is_dually is True
        assert after[3].is_dually is False

        # Verify wheel counts
        assert after[0].number_of_wheels() == 6   # dually Tundra
        assert after[1].number_of_wheels() == 4   # non-dually Civic
        assert after[2].number_of_wheels() == 4   # non-dually M3 Limited
        assert after[3].number_of_wheels() == 4   # non-dually F150

        # Verify how_far_with
        assert after[2].how_far_with(10) == pytest.approx(300.0)  # M3: 30 mpg
        
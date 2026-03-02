from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel

class Truck(Vehicle):
    """
    Represent a truck type of vehicle
    """

    # constructor
    def __init__(self,
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float,
                 is_dually: bool = False # Additional attribution
    ):
        super().__init__(manufacturer, model, mpg)
        self._is_dually = is_dually

    @property
    def is_dually(self) -> bool:
        return self._is_dually

    # specifying the abstract method with truck's condition
    def number_of_wheels(self) -> int:
        return 6 if self._is_dually == True else 4
    
    # printing truck
    def __str__(self) -> str:
        return (
            f"({self._manufacturer}) {self._model}, mpg: {self._mpg:.2f}"
            f" is dually truck: {self._is_dually}"
        )
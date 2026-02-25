from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel

class Sedan(Vehicle):
    """
    Represents a sedan type of vehicle
    """

    # constructor
    def __init__(self,
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float):
        super().__init__(manufacturer, model, mpg)

    # specifying the abstract method
    def number_of_wheels(self) -> int:
        return 4
    
    # printing sedan
    def __str__(self) -> str:
        return (
            f"({self._manufacturer}) {self._model}, mpg: {self._mpg:.2f}"
        )
        
"""
Represents an automodel
"""

class AutoModel:
    def __init__(
            self, 
            name: str, 
            in_production: bool, 
            years: list[int]
            ):
        self._name = name
        self._in_production = in_production
        self._years = list(years) # defensive copy

    @property
    def get_name(self) -> str:
        return self._name
    
    @property
    def get_in_production(self) -> bool:
        return self._in_production
    
    @property
    def get_years(self) -> list[int]:
        return list(self._years) # return a copy
    
    # F150 in production = True, release year: 2020
    def __str__(self) -> str:
        return f"{self._name} in production = {self._in_production}, release year: {self._years[0]}"
        
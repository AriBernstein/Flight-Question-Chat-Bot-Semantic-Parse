from typing import Type
from DataStructures.LocationTypes import USState, City, Airport
from DataStructures.KnowledgeStructures.KnowledgeTypeBase import Knowledge
from Utils.CustomExceptions import InvalidTypeException


class StateKnowledge(Knowledge):
    def __init__(self, is_destination:bool=None) -> None:
        super().__init__(is_destination=is_destination, priority=1)
        self._state = None
        
    def set_state(self, state:USState) -> None:
        if not isinstance(state, USState):
            raise InvalidTypeException(str(Type(USState)), "USState")
        self._state = state
        
    def state_obj(self) -> USState:
        return self._state
       
    def info_str(self) -> str:
        return f"{str(self._state)}, {self.base_info_str}"
    
    def __str__(self) -> str:
        if self._state:
            return f"StateKnowledge: {self.info_str()}"
        return "StateKnowledge: empty"
        
    def __repr__(self) -> str:
        return str(self)

class OriginStateKnowledge(StateKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=False)
    def __str__(self) -> str:
        return "Origin" + super().__str__()

class DestinationStateKnowledge(StateKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=True)
    def __str__(self) -> str:
        return "Destination" + super().__str__()
    
    
class CityKnowledge(Knowledge):
    def __init__(self, is_destination:bool=None) -> None:
        super().__init__(is_destination=is_destination, priority=2)
        self._city = None
        
    def set_city(self, city:City) -> None:
        if not isinstance(city, City):
            raise InvalidTypeException(str(Type(city)), "City")
        self._city = city
        
    def city_obj(self) -> City:
        return self._city
    
    def __str__(self) -> str:
        if self._city:
            return f"CityKnowledge: {str(self._city)}, {self.base_info_str}"
        return f"CityKnowledge: empty"
    
    def __repr__(self) -> str:
        return str(self)
        
class OriginCityKnowledge(CityKnowledge):
    def __init__(self) -> None:
        super().__init__(origin=True)
    def __str__(self) -> str:
        return "Origin" + super().__str__()

class DestinationCityKnowledge(CityKnowledge):
    def __init__(self) -> None:
        super().__init__(origin=False)
    def __str__(self) -> str:
        return "Destination" + super().__str__()
    
    
class AirportKnowledge(Knowledge):
    
    def __init__(self, is_destination:bool=None) -> None:
        super().__init__(is_destination=is_destination, priority=1)
        self._airport = None
        
    def set_airport(self, airport:Airport) -> None:
        if not isinstance(airport, Airport):
            raise InvalidTypeException(str(Type(Airport)), "Airport")
        
        self._airport = airport
        
    def airport_obj(self) -> Airport:
        return self._airport
    
    def __str__(self) -> str:
        if self._airport:
            return f"AirportKnowledge: {str(self._airport)}, {self.base_info_str}"
        return f"AirportKnowledge: empty"
    
    def __repr__(self) -> str:
        return str(self)
    
class OriginAirportKnowledge(AirportKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=False)
    def __str__(self) -> str:
        return "Origin" + super().__str__()

class DestinationAirportKnowledge(CityKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=True)
    def __str__(self) -> str:
        return "Destination" + super().__str__()
from DataStructures.FlightLocations.Locations import State, City, Airport

class Knowledge:
    def __init__(self) -> None:
        self._relevant = True
        self._known = False
        
    def relevant(self) -> bool:
        return self._relevant
    
    def known(self) -> bool:
        return self._known
    
    def make_known(self) -> None:
        self._known = True
        
    def base_info_str(self) -> str:
        if not self._relevant:
            return "irrelevant"
        known_str = "known" if self._known else "unknown"
        return f"relevant, and currently {known_str}"
    
    def __str__(self) -> str:
        return "Base Knowledge class instance. You're probably looking for " + \
            "one of my children."
    
    def __repr__(self) -> str:
        return str(self)
    
    
class StateKnowledge(Knowledge):
    def __init__(self) -> None:
        super().__init__()
        self._state = None
        
    def set_state(self, state:State) -> None:
        self._state = state
        
    def state_obj(self) -> State:
        return self._state
    
    def info_str(self) -> str:
        return f"{str(self._state)}, {self.base_info_str}"
    
    def __str__(self) -> str:
        if self._state:
            return f"StateKnowledge: {self.info_str()}"
        return "StateKnowledge: empty"
        
    def __repr__(self) -> str:
        return str(self)
    
    
class CityKnowledge(Knowledge):
    
    def __init__(self) -> None:
        super().__init__()
        self._city = None
        
    def set_city(self, city:City) -> None:
        self._city = city
        
    def city_obj(self) -> City:
        return self._city
    
    def __str__(self) -> str:
        if self._city:
            return f"CityKnowledge: {str(self._city)}, {self.base_info_str}"
        return f"CityKnowledge: empty"
    
    def __repr__(self) -> str:
        return str(self)
    
    
class AirportKnowledge(Knowledge):
    
    def __init__(self) -> None:
        super().__init__()
        self._airport = None
        
    def airport_city(self, airport:Airport) -> None:
        self._airport = airport
        
    def airport_obj(self) -> Airport:
        return self._airport
    
    def __str__(self) -> str:
        if self._airport:
            return f"AirportKnowledge: {str(self._airport)}, {self.base_info_str}"
        return f"AirportKnowledge: empty"
    
    def __repr__(self) -> str:
        return str(self)
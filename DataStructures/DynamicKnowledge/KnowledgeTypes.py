from datetime import date, time

from DataStructures.FlightLocations.Locations import USState, City, Airport

class OriginDestinationException(Exception):
    def __init__(self) -> None:
        super().__init__("Only call this method on OrigStateKnowledge, " + \
                "DestStateKnowledge, OrigCityKnowledge, DestCityKnowledge, " + \
                    "OrigAirportKnowledge, DestAirportKnowledge")

class Knowledge:
    def __init__(self, is_destination:bool=None, priority:int=-1) -> None:
        self._relevant = True
        self._known = False
        self._is_destination = is_destination
        self._priority=priority
        
    def relevant(self) -> bool:
        return self._relevant
    
    def known(self) -> bool:
        return self._known
    
    def make_known(self) -> None:
        self._known = True
        
    def priority(self) ->int:
        return self._priority
        
    def base_info_str(self) -> str:
        if not self._relevant:
            return "irrelevant"
        known_str = "known" if self._known else "unknown"
        return f"relevant, and currently {known_str}"
    
    def is_base_type():
        return True
    
    def is_destination(self) -> bool:
        if self._is_destination is None: raise OriginDestinationException
        return self._is_destination
    
    def is_origin(self) -> bool:
        if self._is_destination is None: raise OriginDestinationException
        return not self._is_destination
        
    def __str__(self) -> str:
        return "Base Knowledge class instance. You're probably looking for " + \
            "one of my children."
    
    def __repr__(self) -> str:
        return str(self)



class StateKnowledge(Knowledge):
    def __init__(self, is_destination:bool=None) -> None:
        super().__init__(is_destination=is_destination, priority=1)
        self._state = None
        
    def set_state(self, state:USState) -> None:
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
    
    
class TimeKnowledge(Knowledge):
    def __init__(self, is_destination:bool=None) -> None:
        self._time = None   # type: time
        super().__init__(is_destination)
        
    def set_time(self, t:time) -> None:
        self._time = t
    
    def time(self) -> time:
        return self._time
    
    def __str__(self) -> str:
        if self._time:
            t = self._time.strftime("%H:%M")
            return f"TimeKnowledge: {t}, {self.base_info_str()}"
        return "TimeKnowledge: Empty"
    
    def __repr__(self) -> str:
        return str(self)

class OriginTimeKnowledge(TimeKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=False)
    def __str__(self) -> str:
        return "Origin" + super().__str__()
    
class DestinationTimeKnowledge(TimeKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=False)
    def __str__(self) -> str:
        return "Destination" + super().__str__()
    
    
class DateKnowledge(Knowledge):
    def __init__(self, is_destination:bool=None) -> None:
        self._date = None   # type: time
        super().__init__(is_destination)
        
    def set_date(self, d:date) -> None:
        self._date = d
    
    def date(self) -> date:
        return self._date
    
    def __str__(self) -> str:
        if self._date:
            t = self._date.strftime("%b %d %Y")
            return f"TimeKnowledge: {t}, {self.base_info_str()}"
        return "TimeKnowledge: Empty"
    
    def __repr__(self) -> str:
        return str(self)

class OriginDateKnowledge(DateKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=False)
    def __str__(self) -> str:
        return "Origin" + super().__str__()
    
class DestinationDateKnowledge(DateKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=False)
    def __str__(self) -> str:
        return "Destination" + super().__str__()
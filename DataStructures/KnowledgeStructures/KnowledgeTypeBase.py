
from datetime import date, time
from typing import Union

from DataStructures.LocationTypes import City, Country, USState
from Utils.CustomExceptions import OriginDestinationException

class Knowledge:
    def __init__(self, value:Union[Country, USState, City, date, time]=None, 
                 is_destination:bool=None, priority:int=-1) -> None:
        self._relevant = True
        self._is_destination = is_destination
        self._priority=priority
        self._value = value
        
    def relevant(self) -> bool:
        return self._relevant
    
    def known(self) -> bool:
        return self._value is not None
    
    def value(self) -> Union[Country, USState, City, date, time]:
        return self._value
        
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
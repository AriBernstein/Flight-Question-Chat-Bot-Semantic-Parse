
from datetime import date, time
from typing import Union

from DataStructures.LocationTypes import City, Country, USState
from Utils.CustomExceptions import OriginDestinationException

"""
Class representing our knowledge of the world, ie the individual pieces of
flight-travel-related semantic information for which to look during a 
conversation.   """

class Knowledge:
    """
    Fields:
        _relevant (bool): 
            If true (default), then we are either looking for or currently have
            this piece of information. If false, we don't care about this piece 
            of information and will not look for it during semantic analysis.
            There are two reasons it may evaluate to False:
                1) This info is contained within a higher priority subclass 
                   instance. (See _priority field below.)
                2) Parser has recognized a query that doesn't require this info.
        
        _id_destination (bool):
            Knowledge instances are generally in the context of a starting
            (departure), or a destination. If true (default), then this instance
            is associated with the destination Country, USState, City, date, or 
            time. If false, then it is associated with the departure...
            
        __priority (int):
            Integer correlating with the value type; some expected location 
            classes are subclasses/super classes of each other and, as such, are
            inclusive of each other. -1 if no priority (default.). 
            
            If we fill in a Knowledge type of a given priority, we mark all 
            other Knowledge instances of lower priority as irrelevant.  """
            
    def __init__(self, value:Union[Country, USState, City, date, time]=None, 
                 is_destination:bool=None, priority:int=-1) -> None:
        self._relevant = True
        self._is_destination = is_destination
        self._priority=priority
        self._value = value
        
    def relevant(self) -> bool:
        """
        Returns: bool:
            True if currently looking for this piece of info. False otherwise.
        """
        return self._relevant
    
    def known(self) -> bool:
        """
        Returns:
            bool: True if _value field is populated, False otherwise.   """
        return self._value is not None
    
    def value(self) -> Union[Country, USState, City, date, time]:
        """
        Returns: Union[Country, USState, City, date, time]:
            Piece of information represented by this Knowledge instance.    """
        return self._value
        
    def priority(self) ->int:
        """
        Returns: int: 
            Int correlating with _value field type. See class description.  """
        return self._priority
        
    def base_info_str(self) -> str:
        """
        Returns: str: String w/ information about this Knowledge instance.  """
        if not self._relevant:
            return "irrelevant"
        known_str = "known" if self._known else "unknown"
        return f"relevant, and currently {known_str}"
        
    def is_destination(self) -> bool:
        """
        Returns: bool: 
            True if value is associated w/ a destination local/time, False 
            otherwise.  """
        if self._is_destination is None: raise OriginDestinationException
        return self._is_destination
    
    def is_origin(self) -> bool:
        """
        Returns: bool: 
            True if value is associated w/ a origin local/time, False otherwise.
        """
        if self._is_destination is None: raise OriginDestinationException
        return not self._is_destination
        
    def __str__(self) -> str:
        return "Base Knowledge class instance. You're probably looking for " + \
            "one of my children."
    
    def __repr__(self) -> str:
        return str(self)